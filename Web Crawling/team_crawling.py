from bs4 import BeautifulSoup
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import pandas as pd
import urllib.request
import requests
import time
import re
import platform

#chatgpt
# driver=webdriver.Chrome()
# driver.get('https://www.google.com')
# search_box.send_keys('chatgpt')
# search_box.submit()
# log_in=driver.find_element(By.CLASS_NAME,'gb_ha.gb_ia.gb_ee.gb_ed')
# log_in.click()
# driver.find_element(By.CLASS_NAME,'whsOnd.zHQkBf').send_keys('hoon3747@gmail.com')
# next=driver.find_element(By.CLASS_NAME,'VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.qIypjc.TrZEUc.lw1w4b')
# next.click()

driver=webdriver.Chrome()
driver.get('https://www.google.com')
search_box = driver.find_element(By.NAME,'q')
search_box.send_keys('KDnuggets')
search_box.submit()

#kdnuggets
driver.find_element(By.CLASS_NAME,'TbwUpd.NJjxre').click()

#topics
driver.find_element(By.ID,'menu-item-138105').click()

#scroll 내리기
driver.find_element(By.XPATH,'//*[@id="post-106308"]/table/tbody/tr/td/ul/li[8]/div/a').click()

#machine learning
driver.find_element(By.XPATH,'//*[@id="post-106308"]/table/tbody/tr/td/ul/li[6]/div/a').click()

#7 smote oversampling
driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[1]/a').click()
smote=[]
for i in range(1,8):
    smote.append(driver.find_element(By.XPATH,f'//*[@id="post-"]/h2[{i}]').text[2:])
smote
driver.back()

#optimization
driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[5]/a').click()
driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[3]/a').click()
optimization=[]
for i in range(8,18):
    optimization.append(driver.find_element(By.XPATH,f'//*[@id="post-"]/h2[{i}]').text)
optimization
driver.back()

#7 super cheat sheet wordcloud
a=driver.find_elements(By.XPATH,'//*[@id="content"]')
a[1].text

driver.quit()



