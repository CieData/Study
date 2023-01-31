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
time.sleep(1)
driver.get('https://www.google.com')
time.sleep(1)
search_box = driver.find_element(By.NAME,'q')
search_box.send_keys('KDnuggets')
search_box.submit()

#kdnuggets
#https://www.kdnuggets.com/
driver.find_element(By.CLASS_NAME,'TbwUpd.NJjxre').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="boxzilla-82996"]/span').click()
#topics
driver.find_element(By.ID,'menu-item-138105').click()

#필요 매개변수들
i=140
j=1
driver.execute_script(f"window.scrollTo(0,{i})")
title=[]
info=[]
date=[]
cate=[]

#machine learning
while j!=13:
    i+=140
    driver.execute_script(f"window.scrollTo(0,{i})")
    time.sleep(1)
    driver.find_element(By.XPATH,f'//*[@id="post-106308"]/table/tbody/tr/td/ul/li[{j}]/div/a').click()
    time.sleep(1)
    for k in range(1,11):
        title.append(driver.find_element(By.XPATH,f'//*[@id="content"]/ul/li[{k}]/a/b').text)
        info.append(driver.find_element(By.XPATH,f'//*[@id="content"]/ul/li[{k}]/div').text)
        date.append(driver.find_element(By.XPATH,f'//*[@id="content"]/ul/li[{k}]/font').text)
        cate.append(driver.find_element(By.XPATH,f'//*[@id="content"]/ul/li[{k}]/p/span/a').text)
    driver.back()
    time.sleep(1)
    if j==6:
        driver.find_element(By.XPATH,f'//*[@id="post-106308"]/table/tbody/tr/td/ul/li[{j}]/div/a').click()
        time.sleep(1)
        #7 smote oversampling
        #https://www.kdnuggets.com/2023/01/7-smote-variations-oversampling.html
        driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[1]/a').click()
        time.sleep(1)
        smote=[]
        for x in range(1,8):
            smote.append(driver.find_element(By.XPATH,f'//*[@id="post-"]/h2[{x}]').text[2:])
        driver.back()
        time.sleep(1)

        #optimization
        #https://www.kdnuggets.com/2023/01/hyperparameter-optimization-10-top-python-libraries.html
        driver.execute_script(f"window.scrollTo(0,250)")
        driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[3]/a').click()
        time.sleep(1)
        optimization=[]
        for x in range(8,18):
            optimization.append(driver.find_element(By.XPATH,f'//*[@id="post-"]/h2[{x}]').text)
        driver.back()
        time.sleep(1)

        #24 Free book to understand ML
        #https://www.kdnuggets.com/2020/03/24-best-free-books-understand-machine-learning.html
        driver.execute_script(f"window.scrollTo(0,2000)")
        driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[15]/a').click()
        time.sleep(1)
        book=[]
        for x in driver.find_elements(By.XPATH,'//*[@id="post-"]/h1'):
            book.append(x.text[4:])
        driver.back()
        time.sleep(1)


        #7 super cheat sheet
        #https://www.kdnuggets.com/2022/12/7-super-cheat-sheets-need-ace-machine-learning-interview.html

        text=[]
        driver.execute_script(f"window.scrollTo(0,2500)")
        driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[18]/a').click()
        time.sleep(1)
        a=driver.find_elements(By.XPATH,'//*[@id="post-"]/p')
        b=driver.find_elements(By.XPATH,'//*[@id="post-"]/ol')
        for x in b:
            y=x.text.split('\n')
            for k in y:
                text.append(k)
        for x in a:
            y=x.text.split()
            for k in y:
                text.append(k)
        driver.back()
        driver.back()
        time.sleep(1)
    j+=1

preresult=title+info+smote+optimization+book+text
result=[]
for i in preresult:
    a=i.split()
    for j in a:
        result.append(j.lower())
result

from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
english_stops = set(stopwords.words('english'))
result2 = [word for word in result if word not in english_stops] 

count=Counter(result2)
count
tags = count.most_common(40)
tags

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

a=pd.DataFrame(zip(title,info,cate,date))
a.columns=['title','info','topic','date']
a.to_csv('kdn.csv',index=False)