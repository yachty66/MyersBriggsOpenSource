import requests
import time
import random
import re
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

while True:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/Applications/AppicationsMe/Google Chrome.app/Contents/MacOS/Google Chrome"
    driver = webdriver.Chrome(executable_path='/Users/maxhager/Applications/AppicationsMe/chromedriver_mac_arm64/chromedriver', chrome_options=chrome_options)
    url = 'https://www.16personalities.com/free-personality-test'

    driver.get(url)
    time.sleep(2)

    l_with_all_questions_and_answers = []

    for i in range(0, 10):
        results = []
        agree_max_buttons = driver.find_elements("xpath", '//div[@aria-label="agree max"]')
        agree_med_buttons = driver.find_elements("xpath", '//div[@aria-label="agree med"]')
        agree_min_buttons = driver.find_elements("xpath", '//div[@aria-label="agree min"]')
        agree_neutral_buttons = driver.find_elements("xpath", '//div[@aria-label="neutral"]')
        disagree_max_buttons = driver.find_elements("xpath", '//div[@aria-label="disagree max"]')
        disagree_med_buttons = driver.find_elements("xpath", '//div[@aria-label="disagree med"]')
        disagree_min_buttons = driver.find_elements("xpath", '//div[@aria-label="disagree min"]')
        l_with_options = [agree_max_buttons, agree_med_buttons, agree_min_buttons, agree_neutral_buttons, disagree_max_buttons, disagree_med_buttons, disagree_min_buttons]
        html_content = driver.page_source
        pattern = r'<div data-v-7250ab3f="" class="statement"><span.*?>(.*?)</span>'
        results = re.findall(pattern, html_content)
        
        for i in range(0, 6):
            click_button = random.choice(l_with_options)
            click_button[i].click()
            l_with_all_questions_and_answers.append(results[i])
            l_with_all_questions_and_answers.append(click_button[i].get_attribute("aria-label"))
            
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="sp-action sp-button button--action button--purple button--lg button--pill button--fixed button--icon-rt"]'))
        )
        next_button.click()
        time.sleep(2)
        
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    personality_code = soup.find('span', {'class': 'type__code'})
    title = personality_code.text.strip()
    l_with_all_questions_and_answers.append(title)
    with open("results.txt", "a") as file:
        line = ";".join(l_with_all_questions_and_answers).replace("\n", "")
        file.write("%s\n" % line)

    #driver.quit()
