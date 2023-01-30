from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import urllib.request

###javascript이용

driver=webdriver.Chrome()
driver.get('https://www.coffeebeankorea.com/store/store.asp')
driver.execute_script('storePop2(1)')

html = driver.page_source # page_source: 해당 웹페이지의 소스가 저장됨
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify()) # HTML 소스를 보기 좋게 출력


store_names = soup.select('div.store_txt > p.name > span')
store_name_list = []
for name in store_names:
    store_name_list.append(name.get_text())

print('매장 개수: ', len(store_name_list))
print(store_name_list)
store_addresses = soup.select('p.address > span')
store_address_list = []
for addr in store_addresses:
    print(addr.get_text())

driver.quit() # web driver 종료

