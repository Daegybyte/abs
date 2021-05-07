from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

search = ["corgis", "corgi play", "corgi pirates", "corgi loaf", "corgi butt", "corgi sleeping", "puppies", "cute dogs", "cute cat", "kittens", "manatees"]
website = ["youtube","google"]

# rand = int(random.randint(0,len(search)-1))

# driver = webdriver.Chrome()

# # search Google images
# driver.get('https://www.google.com/imghp?hl=en&ogbl') # goes to the google images page

# gsearchbox = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input') # navigates to searchbox

# gsearchbox.send_keys(search[rand]) # enters element from search array

# gsearchbox.send_keys(Keys.RETURN) #enter key to start image search



# search Youtube
# driver.get('https://youtube.com')

# ytsearchbox = driver.find_element_by_xpath('//*[@id="search"]')
# ytsearchbox.send_keys(search[rand])

# ytsearchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# ytsearchButton.click()








pickSearch = int(random.randint(0,len(search)-1))
pickWeb = int(random.randit(0,2))

driver = webdriver.Chrome()

if (pickWeb == 1 ):
    # search Google images
    driver.get('https://www.google.com/imghp?hl=en&ogbl') # goes to the google images page

    gsearchbox = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input') # navigates to searchbox

    gsearchbox.send_keys(search[pickSearch]) # enters element from search array

    gsearchbox.send_keys(Keys.RETURN) #enter key to start image search
else:
    #search Youtube
    driver.get('https://youtube.com')

    ytsearchbox = driver.find_element_by_xpath('//*[@id="search"]')
    ytsearchbox.send_keys(search[pickSearch])

    ytsearchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    ytsearchButton.click()