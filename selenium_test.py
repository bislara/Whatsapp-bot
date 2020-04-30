# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:08:46 2020

@author: LARA
"""

from selenium import webdriver

browser = webdriver.Chrome("/Users/LARA/Downloads/Compressed/chromedriver_win32/chromedriver")

browser.get("https://cyborg.nitrkl.ac.in")

download = browser.find_element_by_link_text("Events")
download.click()

search = browser.find_element_by_id("ID NAME")
search.send_keys("Search name")
