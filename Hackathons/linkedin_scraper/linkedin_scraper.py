import argparse
import time
import json
from typing import List, Dict
import re
from datetime import datetime

# Try to import Playwright first, fallback to Selenium
try:
    from playwright.sync_api import sync_playwright
    USE_PLAYWRIGHT = True
except ImportError:
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.chrome.options import Options
        USE_PLAYWRIGHT = False
    except ImportError:
        raise ImportError("Either Playwright or Selenium is required. Please install one of them.")

# Google Sheets integration
try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    GOOGLE_SHEETS_AVAILABLE = True
except ImportError:
    GOOGLE_SHEETS_AVAILABLE = False
    print("Warning: Google Sheets integration not available. Please install gspread and oauth2client to enable this feature.")


class LinkedInScraper:
    def __init__(self, headless=True):
        self.headless = headless
        self.results = []
    
    def scrape_with_playwright(self, keywords: str, num_results: int = 10) -> List[Dict]:
        """Scrape LinkedIn using Playwright
        
        A real implementation would:
        1. Log in to LinkedIn using credentials
        2. Navigate to https://www.linkedin.com/search/results/people/
        3. Fill search keywords in the search box
        4. Parse search results from the page
        5. Extract name, role, company, and profile URL for each result
        6. Handle pagination to get more results
        7. Add delays between requests to avoid being blocked
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            
            # Navigate to LinkedIn (note: actual scraping would require login)
            # This is a simplified example - real implementation would need authentication
            page.goto("https://www.linkedin.com")
            
            # This is where you would implement the actual search logic
            # For now, we'll return mock data to demonstrate the structure
            results = self._generate_mock_data(keywords, num_results)
            
            browser.close()
            return results
    
    def scrape_with_selenium(self, keywords: str, num_results: int = 10) -> List[Dict]:
        """Scrape LinkedIn using Selenium
        
        A real implementation would:
        1. Log in to LinkedIn using credentials
        2. Navigate to https://www.linkedin.com/search/results/people/
        3. Fill search keywords in the search box
        4. Parse search results from the page
        5. Extract name, role, company, and profile URL for each result
        6. Handle pagination to get more results
        7. Add delays between requests to avoid being blocked
        """
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 10)
        
        try:
            # Navigate to LinkedIn (note: actual scraping would require login)
            driver.get("https://www.linkedin.com")
            
            # This is where you would implement the actual search logic
            # For now, we'll return mock data to demonstrate the structure
            results = self._generate_mock_data(keywords, num_results)
            
            return results
        finally:
            driver.quit()
    
    def _generate_mock_data(self, keywords: str, num_results: int) -> List[Dict]:
        """Generate mock data for demonstration purposes"""
        # In a real implementation, this would be replaced with actual scraping logic
        mock_results = []
        for i in range(num_results):
            mock_results.append({
                "name": f"Person {i+1}",
                "role": f"AI Engineer at Company {i+1}",
                "company": f"Company {i+1}",
                "profile_url": f"https://www.linkedin.com/in/person-{i+1}",
                "contact_status": "Not Contacted",
                "message_date": ""
            })
        return mock_results
    
    def search(self, keywords: str, num_results: int = 10) -> List[Dict]:
        """Perform LinkedIn search with given keywords"""
        print(f"Searching LinkedIn for: {keywords}")
        
        if USE_PLAYWRIGHT:
            results = self.scrape_with_playwright(keywords, num_results)
        else:
            results = self.scrape_with_selenium(keywords, num_results)
        
        self.results = results
        return results
    
    def update_contact_status(self, index: int, status: str, message_date: str = None):
        """Update contact status and message date for a specific result"""
        if 0 <= index < len(self.results):
            self.results[index]["contact_status"] = status
            if message_date:
                self.results[index]["message_date"] = message_date
            else:
                # If no date provided, use current date
                self.results[index]["message_date"] = datetime.now().strftime("%Y-%m-%d")
            print(f"Updated contact status for {self.results[index]['name']} to {status}")
        else:
            print(f"Invalid index: {index}. Must be between 0 and {len(self.results) - 1}")
    
    def save_to_google_sheet(self, sheet_name: str, credentials_file: str):
        """Save results to Google Sheet"""
        if not GOOGLE_SHEETS_AVAILABLE:
            print("Google Sheets integration is not available. Please install required packages.")
            return
        
        # Define the scope
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        
        # Add credentials
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        client = gspread.authorize(creds)
        
        # Open the spreadsheet
        try:
            sheet = client.open(sheet_name).sheet1
        except gspread.SpreadsheetNotFound:
            # Create new spreadsheet if it doesn't exist
            sheet = client.create(sheet_name).sheet1
        
        # Clear existing data
        sheet.clear()
        
        # Add headers
        headers = ["Name", "Role", "Company", "Profile URL", "Contact Status", "Message Date"]
        sheet.append_row(headers)
        
        # Add data
        for result in self.results:
            row = [
                result.get("name", ""),
                result.get("role", ""),
                result.get("company", ""),
                result.get("profile_url", ""),
                result.get("contact_status", ""),
                result.get("message_date", "")
            ]
            sheet.append_row(row)
        
        print(f"Results saved to Google Sheet: {sheet_name}")


def main():
    parser = argparse.ArgumentParser(description="LinkedIn Search Scraper")
    parser.add_argument("keywords", nargs='?', help="Search keywords (e.g. 'AI CTO France')")
    parser.add_argument("--num-results", type=int, default=10, help="Number of results to fetch (default: 10)")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode")
    parser.add_argument("--sheet-name", help="Google Sheet name to save results")
    parser.add_argument("--credentials", help="Path to Google Sheets credentials JSON file")
    parser.add_argument("--update-status", nargs=3, metavar=("INDEX", "STATUS", "DATE"), 
                        help="Update contact status (index, status, date)")
    
    args = parser.parse_args()
    
    # Create scraper instance
    scraper = LinkedInScraper(headless=args.headless)
    
    # Update contact status if requested
    if args.update_status:
        index, status, date = args.update_status
        try:
            index = int(index) - 1  # Convert to 0-based index
            scraper.update_contact_status(index, status, date if date != "None" else None)
        except ValueError:
            print("Invalid index. Please provide a number.")
            return
    
    # Perform search if keywords provided
    if args.keywords:
        results = scraper.search(args.keywords, args.num_results)
        
        # Print results
        print("\nSearch Results:")
        print("-" * 50)
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['name']}")
            print(f"   Role: {result['role']}")
            print(f"   Company: {result['company']}")
            print(f"   Profile: {result['profile_url']}")
            print(f"   Status: {result['contact_status']}")
            print(f"   Date: {result['message_date']}")
            print()
    else:
        # If no keywords provided and no update requested, show help
        if not args.update_status:
            parser.print_help()
            return
    
    # Save to Google Sheet if requested
    if args.sheet_name and args.credentials:
        scraper.save_to_google_sheet(args.sheet_name, args.credentials)


if __name__ == "__main__":
    main()
