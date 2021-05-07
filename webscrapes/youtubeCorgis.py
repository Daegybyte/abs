from selenium import webdriver
import random

rand = random.randint(1,4)
driver = webdriver.Chrome()

driver.get('https://youtube.com')
searchbox = driver.find_element_by_xpath('//*[@id="search"]')

# Search terms
if (rand == 1):
    searchbox.send_keys('corgis')
elif (rand == 2):
    searchbox.send_keys('corgi play')
else:
    searchbox.send_keys('corgi pirates')


searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
