from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

def bookDownloader(bookSearch):



   path = "C:\Program Files (x86)/chromedriver.exe"

   #driver = webdriver.Chrome(path)

   options = Options()
   options.headless = True
   driver = webdriver.Chrome(path, options = options)

   driver.get("https://b-ok.cc/")



   search = driver.find_element_by_name("q") #find search box
   search.send_keys(bookSearch) #typing
   search.send_keys(Keys.RETURN) #press enter



   time.sleep(5)



   links =  driver.find_elements_by_xpath("//a[@href]")
   address = []
   for link in links:
      address.append(link.get_attribute("href"))
   driver.get(address[27])



   download = driver.find_element_by_class_name("book-details-button")
   download.click()



   time.sleep(20)



   driver.close()