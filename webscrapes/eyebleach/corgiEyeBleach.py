from selenium import webdriver
import random

search = ["corgis", "corgi play", "corgi pirates", "corgi loaf", "corgi butt", "corgi sleeping"]
rand = int(random.randint(0,len(search)-1))

driver = webdriver.Chrome()

driver.get('https://youtube.com')
searchbox = driver.find_element_by_xpath('//*[@id="search"]')

searchbox.send_keys(search[rand])

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()