import requests
from bs4 import BeautifulSoup


#http://127.0.0.1:5500/sampleSite.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# i need to build the random module
#before i do this i build something to click me through the whole questions and once i have the results i can build the random module
#because than i can be sure that its working


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/AppicationsMe/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(executable_path='/Users/maxhager/Applications/AppicationsMe/chromedriver_mac_arm64/chromedriver', chrome_options=chrome_options)


# Navigate to the example website
url = 'https://www.16personalities.com/free-personality-test'
driver.get(url)

for i in range(0, 10):
    agree_buttons = driver.find_elements("xpath", '//div[@aria-label="agree max"]')
    for button in agree_buttons:
        button.click()
    # Wait for the next button to become clickable
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="sp-action sp-button button--action button--purple button--lg button--pill button--fixed button--icon-rt"]'))
    )
    # Click the next button
    next_button.click()
    time.sleep(2)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
title = soup.title.text.strip()

print(title)


#with open("results.html", "w") as file:
#    file.write(driver.page_source)

#agree_button = driver.find_element("xpath", '//div[@aria-label="agree max"]')

#print(driver.page_source)

driver.quit()
