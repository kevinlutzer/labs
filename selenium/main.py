# This script uses selenium to scrape trading activity for common stocks on
# the nasqaq website. It requires geckodriver and the selenium package.
# Make sure to install the required packages:
# pip install selenium

''' 
Example output:
Symbol: NVDA, Activity: -9.69%, Sentiment: SELL -2
Symbol: TSLA, Activity: +5.16%, Sentiment: BUY +4
Symbol: PLTR, Activity: +3.38%, Sentiment: BUY +10
Symbol: SPY, Activity: +2.04%, Sentiment: BUY +3
Symbol: TQQQ, Activity: +1.81%, Sentiment: BUY +3
'''

import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

service = Service()
driver = webdriver.Firefox(service=service, options=options)

try:

    driver.get("https://www.nasdaq.com/")

    # The table only loads if we scroll down, so do that first and the grab the table element
    # and corresponding rows
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(3)  # Wait for the table to actually load, its done asynchronously.

    # Grab all rows from the table (excluding the header row)
    table = driver.find_element(By.CLASS_NAME, "jupiter22-retail-activity-tracker__table")
    rows = table.find_elements(By.TAG_NAME, 'tr')

    # Iterate for each row in the table
    for idx, row in enumerate(rows[1:], 1):
        cols = row.find_elements(By.TAG_NAME, 'td') 
        cols_text = [col.text.strip() for col in cols]
        
        if len(cols_text) == 3:
            # Print the text of each column
            print(f"Symbol: {cols_text[0]}, Activity: {cols_text[1]}, Sentiment: {cols_text[2]}")

finally:
    driver.quit()