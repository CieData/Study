from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import urllib.request
import pandas as pd


def coffeebean_store(store_list):
    coffeebean_url = 'https://www.coffeebeankorea.com/store/store.asp'
    driver = webdriver.Chrome()
    #자바스크립트 실행
    for i in range(1, 380):
        driver.get(coffeebean_url)
        time.sleep(1) # 웹페이지를 연결할 동안 1초 대기

        driver.execute_script('storePop2(%d)' % i)
        time.sleep(1)
        try:
            html = driver.page_source
            #지점 정보 가져오기
            soup = BeautifulSoup(html, 'html.parser')

            store_name = soup.select_one('div.store_txt > h2').text	# 매장 이름
            store_info = soup.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_addr = store_address_list[0] # 매장 주소
            store_phone = store_info[3].text # 매장 전화번호
            print('{} {} {} {}'.format(i+1, store_name, store_addr, store_phone))
            store_list.append([store_name, store_addr, store_phone])
        except:
            continue

def main():
    store_info = []
    coffeebean_store(store_info)
    # DataFrame으로 변경
    coffeebean_table = pd.DataFrame(store_info, columns=('매장이름', '주소', '전화번호'))
    print(coffeebean_table.head())

    # DataFrame을 csv파일로 저장 (utf-8로 인코딩)
    coffeebean_table.to_csv('coffeebean_branches.csv', encoding='utf-8', mode='w', index=True)
main()
