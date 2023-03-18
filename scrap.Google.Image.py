# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:34:19 2023

@author: Administrator
"""
#Import
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import urllib

#excute google website
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/search?q=car+in+oman+opensooq&tbm=isch&ved=2ahUKEwjHg6vkpoj9AhVqnScCHW4_DS4Q2-cCegQIABAA&oq=car+in+oman+opensooq&gs_lcp=CgNpbWcQA1CJJVjFKGDkKmgAcAB4AIABpwKIAfsGkgEFMC4yLjKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=kdTkY4f3JOq6nsEP7v608AI&bih=685&biw=1396")
time.sleep(5)

#load all website page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(10)

#Find all car images resource 
img1 = driver.find_elements(By.XPATH,"//img[contains(@class,'rg_i Q4LuWd')]")
 
#Determine the number of images that will extract
imgNum = 100   

#If number of images that found not reach images requirment
while len(img1) < imgNum:
    
   #click on show more result button
   b = driver.find_element(By.XPATH,"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/input")
   time.sleep(5)
   driver.execute_script("arguments[0].click();", b);
   time.sleep(5)
   
   #load the page
   driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
   time.sleep(10)
   img1.clear()
   
   #find more images resource
   img1 = driver.find_elements(By.XPATH,"//img[contains(@class,'rg_i Q4LuWd')]")
   time.sleep(5)
   
i=0
#Save images
for img in img1:
    try: 
        img.click()
        time.sleep(10)
        n = driver.find_element(By.XPATH,"/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img")
        
        time.sleep(5)
        src = n.get_attribute('src')
        urllib.request.urlretrieve(str(src),"C:/Users/Administrator/Desktop/carrs/"+str(i)+".jpg") 
        time.sleep(2)
        i = i + 1
    except:
        continue
    
