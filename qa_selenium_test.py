
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest



driver = webdriver.Chrome()
try:

    url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    driver.get(url)

    # Locate the search box
    searchBox = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    searchBox.clear()
    # send the search keys(input)
    searchBox.send_keys("New York")
    time.sleep(3)

    message = driver.find_element(By.XPATH, "//div[@id='example_info']").text
    assert "Showing 1 to 5 of 5 entries (filtered from 24 total entries)" in message



finally:
    #Close the WebDriver
    driver.quit()