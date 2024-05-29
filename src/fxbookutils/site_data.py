from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from src.fxbookutils.row_data import *

HTML_FILE_PATH = f'fxbook.html' # create directory and paste starting with folder name relative to this script

def getRowsFromSite(URL, timezone):
    driver = initializeWebdriver()
    print("\nRetrieving Data... please wait")
    driver.get(URL)
    dropdown = Select(driver.find_element(By.ID, "timezoneoffset"))
    dropdown.select_by_visible_text(timezone)
    time.sleep(.8) # Timer to allow for enough time to retrieve the site
    page = driver.page_source
    with open(HTML_FILE_PATH, 'w', encoding='utf-8') as file:
        file.write(page)
    driver.close()
    print("Data retrieved!")
    return getRows(HTML_FILE_PATH)
    
def initializeWebdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless');
    options.add_argument('log-level=3')
    return webdriver.Chrome(options=options)
