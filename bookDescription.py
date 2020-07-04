from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

def bookDescription(bookSearch):




   path = "C:\Program Files (x86)/chromedriver.exe"
   #driver = webdriver.Chrome(path)

   options = Options()
   options.headless = True
   driver = webdriver.Chrome(path, options = options)

   driver.get("https://books.google.com/")



   search = driver.find_element_by_id("oc-search-input") #find search box
   search.send_keys(bookSearch) #typing
   search.send_keys(Keys.RETURN) #press enter



   links =  driver.find_elements_by_xpath("//a[@href]")
   address = []
   for link in links:
      address.append(link.get_attribute("href"))



   driver.get(address[31])
   exit = driver.find_element_by_class_name("kt12b")
   exit.click()



   url = driver.current_url
   source = requests.get(url).text
   html = BeautifulSoup(source, features="html5lib")


   synopsis = html.find('div', id = "synopsistext").text
   return synopsis

