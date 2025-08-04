# LinkedIn Search Scraper

This tool scrapes LinkedIn search results based on keywords and saves them to a Google Sheet. It includes columns for contact status and message date.

## Features

- Search LinkedIn for people based on keywords (e.g., "AI CTO France")
- Extract name, role, company, and profile URL
- Save results to Google Sheets
- Command-line interface for easy usage

## Installation

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. If using Playwright, install the browsers:
   ```
   python -m playwright install
   ```

## Usage

### Basic Search
```
python linkedin_scraper.py "AI CTO France"
```

### Search with Options
```
python linkedin_scraper.py "AI CTO France" --num-results 20 --headless
```

### Save to Google Sheet
```
python linkedin_scraper.py "AI CTO France" --sheet-name "LinkedIn Contacts" --credentials "path/to/credentials.json"
```

### Update Contact Status
```
python linkedin_scraper.py --update-status 1 "Contacted" "2025-08-02"
```

Note: The update-status functionality in this demonstration tool will only work if you've previously run a search in the same session. In a real implementation, you would load existing data from a Google Sheet or other storage.

## Google Sheets Setup

To save results to Google Sheets, you need to:

1. Create a Google Cloud Project
2. Enable the Google Sheets API and Google Drive API
3. Create a service account and download the JSON credentials file
4. Share your Google Sheet with the service account email

## Important Notes

This is a demonstration tool that currently generates mock data. A real implementation would require:

1. LinkedIn account credentials
2. Proper authentication handling
3. Implementation of search and parsing logic
4. Handling of LinkedIn's anti-scraping measures

The mock data functionality is included to demonstrate the tool's structure and Google Sheets integration without violating LinkedIn's terms of service.
