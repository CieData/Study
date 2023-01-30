from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import urllib.request

driver=webdriver.Chrome()
driver.get('https://google.com')
driver.implicitly_wait(3)
search_box = driver.find_element(By.NAME,'q')
search_box.send_keys('빅데이터')
search_box.submit() #	검색어를 전달

### iframe 이동
driver=webdriver.Chrome()
driver.get('https://blog.naver.com/swf1004/221631056531')
driver.switch_to.frame('mainFrame')	# 해당 iframe으로 이동
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
whole_border = soup.find('div', {'id': 'whole-border'})
results = whole_border.find_all('div', {'class': 'se-module'})
result1=[]
for result in results:
    print(result.text.replace('\n', ''))
    result1.append(result.text)