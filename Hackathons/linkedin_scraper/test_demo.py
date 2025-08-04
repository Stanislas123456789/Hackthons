import argparse
from linkedin_scraper import LinkedInScraper

def main():
    # Create scraper instance
    scraper = LinkedInScraper(headless=True)
    
    # Perform a search to generate mock results
    scraper.search("AI CTO France", 5)
    
    # Print initial results
    print("Initial Search Results:")
    print("-" * 50)
    for i, result in enumerate(scraper.results, 1):
        print(f"{i}. {result['name']}")
        print(f"   Role: {result['role']}")
        print(f"   Company: {result['company']}")
        print(f"   Profile: {result['profile_url']}")
        print(f"   Status: {result['contact_status']}")
        print(f"   Date: {result['message_date']}")
        print()
    
    # Update contact status for the first result
    print("Updating contact status for the first result...")
    scraper.update_contact_status(0, "Contacted", "2025-08-02")
    
    # Print updated results
    print("\nUpdated Search Results:")
    print("-" * 50)
    for i, result in enumerate(scraper.results, 1):
        print(f"{i}. {result['name']}")
        print(f"   Role: {result['role']}")
        print(f"   Company: {result['company']}")
        print(f"   Profile: {result['profile_url']}")
        print(f"   Status: {result['contact_status']}")
        print(f"   Date: {result['message_date']}")
        print()

if __name__ == "__main__":
    main()
