from ntpath import join
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import bs4


driverPath = join(os.path.dirname(__file__), 'geckodriver.exe')
driver = webdriver.Firefox(executable_path=driverPath)


driver.get('https://iranfile.ir/search')



data = driver.find_element_by_xpath('//*[@id="dvRegions"]')
time.sleep(2)
data.click()
time.sleep(1)
data = driver.find_element_by_xpath('//*[@id="1,-11,-1"]').find_element_by_tag_name('span')
time.sleep(1)
data.click()
time.sleep(1)


regionList = []
for count in range(0, 130):
    try:
        html = driver.find_element_by_id('1,' + str(count) + ',-1').get_attribute('outerHTML')
        soup = bs4.BeautifulSoup(html, features='html.parser')
        regionList.append(soup.text)
        print(soup.text)
    except:
        pass


driver.get('https://iranfile.ir/search')

type = driver.find_element_by_xpath('/html/body/div[2]/section[1]/form/div/div/div[1]/div[5]/div/button')
time.sleep(5)
type.click()
time.sleep(1)
type = driver.find_element_by_xpath('/html/body/div[2]/section[1]/form/div/div/div[1]/div[5]/div/div/ul').find_elements_by_tag_name('li')
time.sleep(1)

typeList = []
for t in type:
    typeList.append(t.text)


regionFile = open('regionList.txt', 'w', encoding='utf8')
for region in regionList:
    regionFile.write(str(region) + ';')
regionFile.close()

typeFile = open('typeList.txt', 'w', encoding='utf8')
for type in typeList:
    typeFile.write(str(type) + ';')
typeFile.close()