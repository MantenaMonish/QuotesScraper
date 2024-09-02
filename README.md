# QuotesScraper

## Overview
QuotesScraper is a Python web scraping tool that extracts quotes and author information from the "Quotes to Scrape" website. Using the `requests` library for HTTP requests and `BeautifulSoup` for HTML parsing, this project gathers quotes, authors, and related tags efficiently.

## Features
- **Scrapes Quotes:** Extracts quotes, authors, and tags from quote pages.
- **Extracts Author Information:** Gathers details about authors including name, date of birth, location, and description.
- **Handles Pagination:** Automatically traverses through multiple pages of quotes.

## Requirements
- Python 3.x
- Requests
- BeautifulSoup4

## Code Overview

- **`clean(url)`**: Normalizes and extracts a clean identifier from the author URL.
- **`scrape_quote(html_soup)`**: Extracts quotes, authors, and tags from quote pages. Adds authors to the `authors_seen` set.
- **`scrape_author(author_soup, author_id)`**: Extracts detailed information about authors from their respective pages.
- **Main Loop**: Iterates through quote pages, handles pagination, and scrapes author details.

## Example

After running the script, it will output detailed information including:

- **Quote**: The text of the quote.
- **Author**: The name of the author.
- **Tags**: Associated tags for the quote.

**Author Details**:
- **Name**: The author's name.
- **Date of Birth**: The author's date of birth.
- **Location**: The author's location.
- **Description**: A brief description of the author.

## License

This project is licensed under the MIT License.


