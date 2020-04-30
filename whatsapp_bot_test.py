# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:46:34 2020

@author: LARA
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("/Users/LARA/Downloads/Compressed/chromedriver_win32/chromedriver")
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser,600)
#browser.quit()
 
target ='"TEST"'
string = "HIIIIIIIII!!!"
#x_arg = "//span[@title="+target+"]"
#target = wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))
# Select the target
x_arg = '//span[contains(@title,' + target + ')]'
wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))

browser.find_element_by_xpath(x_arg).click()


print(target)
target.click()