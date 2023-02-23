import requests
from bs4 import BeautifulSoup


#http://127.0.0.1:5500/sampleSite.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/AppicationsMe/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(executable_path='/Users/maxhager/Applications/AppicationsMe/chromedriver_mac_arm64/chromedriver', chrome_options=chrome_options)


# Navigate to the example website
url = 'https://www.16personalities.com/free-personality-test'
driver.get(url)


time.sleep(2)
agree_button = driver.find_element("xpath", '//div[@aria-label="agree max"]')
agree_button.click()

time.sleep(2)


#load driver.page_source into a html file
#with open('test.html', 'w') as f:
#    f.write(driver.page_source)


#print(driver.current_url)
#print(driver.page_source)
time.sleep(5)

#click_me_button = WebDriverWait(driver, 10).until(
#    EC.element_to_be_clickable((By.ID, 'click-me'))
#)
#click_me_button.click()

#time.sleep(5)


driver.quit()
