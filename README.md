# Web Scraping and Text Sequencing

This Python script utilizes BeautifulSoup and Selenium libraries for web scraping from a list of Wikipedia URLs. It then processes the text data and creates text sequences along with their corresponding targets, saving them to a CSV file for pre-training data.

## Requirements
- Python 3
- BeautifulSoup (`bs4`)
- Selenium (`selenium`)
- `keyboard` library
- `requests` library

## Installation
1. Make sure you have Python 3 installed.
2. Install required libraries using pip:
    ```bash
    pip install beautifulsoup4 selenium keyboard
    ```
3. Clone this repository:
    ```bash
    git clone https://github.com/FogadOg/preTrainingDataScraper.git
    ```

## Usage
1. Modify the `urls` list in the script to include the desired Wikipedia URLs to scrape.
2. Run the script:
    ```bash
    python scraper.py
    ```
3. The script will scrape the specified Wikipedia pages, process the text data, and save the pre-training data to a CSV file named `preTrainingData.csv`.

## Script Overview
- The script defines classes for web scraping and text data processing.
- The `Scrape` class inherits from `WaitForKeyPress`, which waits for the 'esc' key press before proceeding.
- The `Scrape` class scrapes each Wikipedia URL provided in the `urls` list.
- It extracts text data from the main content of each page.
- The text data is cleaned and split into sequences with a specified window size.
- The script saves the sequences along with their targets to a CSV file for further processing.

## Note
- Ensure proper usage of web scraping by reviewing and complying with Wikipedia's terms of service.
- This script is for educational purposes and should be used responsibly.

