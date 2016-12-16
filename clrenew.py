#Welcome to clrenew, a tool to renew your craigslist listings
from selenium import webdriver

# Find Renew links and click them
driver=webdriver.Firefox()
driver.get("https://accounts.craigslist.org/login/home?filter_page=1")
elem1 = driver.find_element_by_link_test("renew")
elem1.click()

print "done, trying next page"

driver=webdriver.Firefox()
driver.get("https://accounts.craigslist.org/login/home?filter_page=2")
elem1 = driver.find_element_by_link_test("renew")
elem1.click()

print "done, your renewal is complete."

