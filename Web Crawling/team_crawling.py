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

driver=webdriver.Chrome()
driver.get('https://www.google.com')
search_box = driver.find_element(By.NAME,'q')
search_box.send_keys('KDnuggets')
search_box.submit()

#kdnuggets
#https://www.kdnuggets.com/
driver.find_element(By.CLASS_NAME,'TbwUpd.NJjxre').click()
driver.find_element(By.XPATH,'//*[@id="boxzilla-82996"]/span').click()
#topics
driver.find_element(By.ID,'menu-item-138105').click()

#scroll 내리기
driver.find_element(By.XPATH,'//*[@id="post-106308"]/table/tbody/tr/td/ul/li[8]/div/a').click()

#machine learning
driver.find_element(By.XPATH,'//*[@id="post-106308"]/table/tbody/tr/td/ul/li[6]/div/a').click()

#7 smote oversampling
#https://www.kdnuggets.com/2023/01/7-smote-variations-oversampling.html
driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[1]/a').click()
smote=[]
for i in range(1,8):
    smote.append(driver.find_element(By.XPATH,f'//*[@id="post-"]/h2[{i}]').text[2:])
smote
driver.back()

#optimization
#https://www.kdnuggets.com/2023/01/hyperparameter-optimization-10-top-python-libraries.html
driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[5]/a').click()
driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[3]/a').click()
optimization=[]
for i in range(8,18):
    optimization.append(driver.find_element(By.XPATH,f'//*[@id="post-"]/h2[{i}]').text)
optimization
driver.back()

#7 super cheat sheet wordcloud
#https://www.kdnuggets.com/2022/12/7-super-cheat-sheets-need-ace-machine-learning-interview.html

text=[]
driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[20]/a').click()
driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[18]/a').click()
a=driver.find_elements(By.XPATH,'//*[@id="post-"]/p')
b=driver.find_elements(By.XPATH,'//*[@id="post-"]/ol')
for i in b:
    j=i.text.split('\n')
    for k in j:
        text.append(k)
for i in a:
    j=i.text.split()
    for k in j:
        text.append(k)
count=Counter(text)
count
tags = count.most_common(40)

if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin': # Mac	OS
    path = r'/System/Library/Fonts/AppleGothic'
else:
    path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

wc = WordCloud(font_path=path, background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

driver.quit()



