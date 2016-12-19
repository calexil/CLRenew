#Welcome to clrenew, a tool to renew your craigslist listings
import os
from selenium import webdriver
import time

# Find Renew links and click them
driver=webdriver.Firefox()

url="https://accounts.craigslist.org/login/home?filter_page=1"
try:
    time.sleep(5)
    driver.get(url)
    element = driver.find_element_by_xpath("//div[@class='manage renew']")
    element.click()
    time.sleep(5)
    element = driver.find_element_by_xpath("//div[@class='manage renew']")
    element.click()
    time.sleep(5)
except Exception as e:
    print e
    driver.quit()
driver.quit()


print "done, trying next page"

#run it again
driver=webdriver.Firefox()

url="https://accounts.craigslist.org/login/home?filter_page=2"
try:
    driver.get(url)
    element = driver.find_element_by_xpath("//div[@class='manage renew']")
    element.click()
    time.sleep(5)
    element = driver.find_element_by_xpath("//div[@class='manage renew']")
    element.click()
    time.sleep(5)
except Exception as e:
    print e
    driver.quit()
driver.quit()


print "done, your renewal is complete."

