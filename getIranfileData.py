import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import requests
import bs4



regionFile = open('regionList.txt', 'r', encoding='utf8')
regions = regionFile.read()
regionList = regions.split(';')
regionFile.close()

typeFile = open('typeList.txt', 'r', encoding='utf8')
types = typeFile.read()
typeList = types.split(';')
typeFile.close()



driverPath = os.path.join(os.path.dirname(__file__), '../geckodriver.exe')
driver = webdriver.Firefox(executable_path=driverPath)
driver.get('https://iranfile.ir/search')



for region in regionList:
    driver.get('https://iranfile.ir/search')
    data = driver.find_element_by_xpath('//*[@id="dvRegions"]')
    time.sleep(1)
    data.click()
    time.sleep(1)
    data = driver.find_element_by_xpath('//*[@id="1,-11,-1"]').find_element_by_tag_name('span')
    time.sleep(1)
    data.click()
    time.sleep(1)
    data = driver.find_element_by_id('txtSearch_regions_popup').send_keys(region)
    time.sleep(1)

    for count in range(0, 130):
        try:
            driver.find_element_by_id('1,'+ str(count) +',-1').click()
            
        except:
            pass

    
    liTagCount = 11
    for li in range(1, liTagCount + 1):
        type = driver.find_element_by_xpath('/html/body/div[2]/section[1]/form/div/div/div[1]/div[5]/div/button')
        time.sleep(1)
        type.click()
        time.sleep(1)

        type = driver.find_element_by_xpath('/html/body/div[2]/section[1]/form/div/div/div[1]/div[5]/div/div/ul/li[' + str(li) + ']')
        time.sleep(1)
        type.click()
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div[2]/section[1]/form/div/div/div[3]/button').click()
        time.sleep(4)

        urlsFile = open('urls.txt', 'a', encoding='utf8')
        urlsFile.write(driver.current_url + '\n')
        urlsFile.close()

    