from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

driver=webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(3)
# id, 비밀번호 전달
# <input>의 이름이 id를 검색
driver.find_element(By.NAME,'id').send_keys('hoon3747')
driver.find_element(By.NAME,'pw').send_keys('dnehal1cls!@')
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()