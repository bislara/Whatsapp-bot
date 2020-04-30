# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 02:45:44 2020

@author: LARA
"""

# import the selenium libraries
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome("/Users/LARA/Downloads/Compressed/chromedriver_win32/chromedriver") 
  
# open the whatsapp website using the link of web whatsapp
driver.get("https://web.whatsapp.com/") 
# wait for 600 milliseconds each time to scan the qr code
wait = WebDriverWait(driver, 600) 
wait5 = WebDriverWait(driver, 50) 
  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
# name should be within double quotes
target = '"Subham Mohanty Nitr"'
  
# Replace the below string with your own message 
string = "Hello!! Message sent by Python"
  
# argument to search in the html tags
x_arg = '//span[contains(@title,' + target + ')]'
# wait untill the search in found
group_title = wait5.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 
group_title.click() 

# select the text box to send the message
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 

# send the message in the text box for 5 times
for i in range(5): 
    input_box.send_keys(string + Keys.ENTER) 
    time.sleep(1) 
    
# send image file path
filepath = 'C:/Users/LARA/Pictures/test.jpg'
# search the attachment link
attachment_section = '//div[@title="Attach"][@role="button"]'
# wait till is found
attachment_box = wait5.until(EC.presence_of_element_located((By.XPATH, attachment_section))) 
attachment_box.click()
# select the image/video tag from that
input_file_xpath = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"][@type="file"]'
photo_btn = wait.until(EC.presence_of_element_located((By.XPATH, input_file_xpath))) 
# send the filepath from laptop to select the file and send
photo_btn.send_keys(filepath)

# click on the send button
send_btn_xpath = '//span[@data-icon="send-light"]'
send_btn = wait.until(EC.presence_of_element_located((By.XPATH, send_btn_xpath))) 
send_btn.click()


# If contact not found, then search for it
searBoxPath = '//div[@class="_2S1VP copyable-text selectable-text"]'
search = wait.until(EC.presence_of_element_located(( By.XPATH, searBoxPath)))
search.send_keys("Subham")
time.sleep(5)
print('Target Searched')

# =============================================================================
# # click the search button
# click_search_path = '/html/body/div/div/div/div[2]/div/div[2]/div/div/div/div[4]'
# # click_search_path = '/html/body/div/div/div/div[2]/div/div[2]/div/button'
# click_search = wait5.until(EC.presence_of_element_located(( By.XPATH, click_search_path)))
# click_search.click()
# 
# =============================================================================

search.clear()






    