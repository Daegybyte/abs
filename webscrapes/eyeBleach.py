# $ pip3 install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import random

search = [
    "corgis", "corgi play", "corgi pirates", "corgi loaf", "corgi butt", "corgi sleeping",
    "puppies", "cute dogs", "cute cat", "kittens", "manatees", "baby animals", "baby goats",
    "baby sloths", "baby turtles", "snakes in hats"
        ]

website = ["google", "youtube"]

pickSearch = int(random.randint(0,len(search)-1))
pickWeb = int(random.randint(0,len(website)-1))

driver = webdriver.Chrome()

if (pickWeb == 0 ):
    # search Google images
    driver.get('https://www.google.com/imghp?hl=en&ogbl') # goes to the google images page

    gSearchbox = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input') # navigates to searchbox

    gSearchbox.send_keys(search[pickSearch]) # enters element from search array

    gSearchbox.send_keys(Keys.RETURN) #enter key to start image search
else:
    #search Youtube
    driver.get('https://youtube.com')

    ytSearchbox = driver.find_element_by_xpath('//*[@id="search"]')
    ytSearchbox.send_keys(search[pickSearch])

    ytSearchbox.send_keys(Keys.RETURN)