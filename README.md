# Amazon Review Web Scraper

This is a Python script that allows you to scrape Amazon product reviews using Selenium.

## Dependencies
To run this script, you need to install the following dependencies:

- `selenium`: Use the following command to install it: `pip install selenium`
- `webdriver_manager`: Use the following command to install it: `pip install webdriver_manager`
- `dotenv`: Use the following command to install it: `pip install dotenv`
## How to Use
To use this web scraper, follow these steps:

1. Create a `.env` file in the project directory.
2. In the `.env` file, enter your Amazon username and password in the following format:
   ```
   AMAZON_USERNAME=your_username
   AMAZON_PASSWORD=your_password
   ```
3. Run the script using Python.
4. Enter the URL of the review page of the Amazon product you want to scrape.
5. The script will scrape the reviews and save the output in a `output.csv` file in the project directory.

**Note:** 
- Make sure you have a stable internet connection and the necessary credentials to access Amazon.
- It is highly recommended to use a VPN (Virtual Private Network) for safety while web scraping from Amazon. Failure to do so may result in IP blocking from Amazon.

## Output
The output of the script is saved in a `output.csv` file. Each row in the CSV file represents a single review and contains the following information:

- Reviewer name
- Review date
- Review rating
- Review title
- Review text

You can open the CSV file using a spreadsheet program like Microsoft Excel or Google Sheets to analyze and process the scraped reviews.

Enjoy scraping Amazon product reviews with this script!