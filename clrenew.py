#Welcome to clrenew, a tool to renew your craigslist listings
import os
import time
from os.path import expanduser
home = expanduser("~")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--user-data-dir=%s' % os.path.join(os.path.expanduser("~"), ".config/chromium/Default" ) )


# Find Renew links and click them
driver = webdriver.Chrome(chrome_options=options)  


url0="https://accounts.craigslist.org/login/home"
url1="https://accounts.craigslist.org/login/home?filter_page=1"
url2="https://accounts.craigslist.org/login/home?filter_page=2"

driver.get(url0)

try:
    time.sleep(5)
    driver.get(url1)
    element = driver.find_element_by_xpath("//*[@id='paginator']/table/tbody/tr[1]/td[2]/div/form[3]/input[3]")
    element.click()
    time.sleep(5)
    element = driver.find_element_by_xpath("//*[@id='paginator']/table/tbody/tr[2]/td[2]/div/form[3]/input[3]")
    element.click()
    time.sleep(10)
except Exception as e:
    print e




print "done, trying next page"

#run it again
try:
    time.sleep(5)
    driver.get(url2)
    element = driver.find_element_by_xpath("//*[@id='paginator']/table/tbody/tr[1]/td[2]/div/form[3]/input[3]")
    element.click()
    time.sleep(5)
    element = driver.find_element_by_xpath("//*[@id='paginator']/table/tbody/tr[2]/td[2]/div/form[3]/input[3]")
    element.click()
    time.sleep(5)
except Exception as e:
    print e

print "done, your renewal is complete."
driver.quit()
