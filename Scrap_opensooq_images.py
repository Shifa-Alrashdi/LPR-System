# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:13:42 2023

@author: Administrator
"""
#Import
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import urllib

#Determine the number of images that will extract
num = 2000  

#excute opensoooq website
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://om.opensooq.com/en/find?page=100&PostSearch[categoryId]=1837&PostSearch[subCategoryId]=1839")
time.sleep(5)

#Load all website page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5) 

#Find advertisement source
img1 = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/main/section[1]/div[2]/div[2]/a/div[1]/img")
time.sleep(5)

#Click the car advertisement
img1.click()
time.sleep(5)

i=0
while i<num:
      #Save all sources of images in the advertisement 
      images = driver.find_elements(By.XPATH,"//img[contains(@class,'image-gallery-image')]")
      src = []
      j =0
      #Save ID of the advertisement 
      text =  driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[4]/div/main/div/section/div[1]/span").text
      textSplit = text.split(" ")
      #Save all images in the advertisement with the ID of the advertisement
      for img2 in images: 
          if img2.get_attribute('src') and 'http' in img2.get_attribute('src') :
              src.append((img2.get_attribute('src')))
              urllib.request.urlretrieve(str(src[j]),"C:/Users/Administrator/Desktop/car5/"+textSplit[2]+"_"+str(j)+".jpg") 
              time.sleep(5)
              i=i+1
              j =j+1
      #Move to the next car advertisement
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")  
      time.sleep(5)  
      try: 
        #Clicl next ad button
        b = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[4]/div/main/div/section/div[2]/a[2]/div/div[1]")
        time.sleep(5)
        driver.execute_script("arguments[0].click();", b);
        time.sleep(5)

      except: 
        #Clicl similar advertisement
        b = driver.find_element(By.XPATH,"//img[contains(@class,'radius-8 width-100 height-100')]")
        time.sleep(5)
        b.click()
        time.sleep(5)
      images.clear()
          
      
      
    

