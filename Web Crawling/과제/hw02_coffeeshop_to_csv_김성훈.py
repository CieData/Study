from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def hollys(url):
    location=[]
    name=[]
    addr=[]
    num=[]
    for i in range(1,54):
        globals()[f'url{i}']=url.format(i)
        original_html = requests.get(globals()[f'url{i}'])
        soup = BeautifulSoup(original_html.text, "html.parser")
        info=soup.select('tr')
        
        for j in range(1,11):
            try:
            #매장이 있는 지역
                location.append(info[j].select('td')[0].text)
            #매장 이름
                name.append(info[j].select('td')[1].text)
            #매장 주소
                addr.append(info[j].select('td')[3].text)
            #매장 전화번호
                num.append(info[j].select('td')[5].text)
            except:
                pass
    result = pd.DataFrame({'매장이름' : name,
                    '위치(시,구)' : location,
                    '주소' : addr,
                    '전화번호' : num})
    result.to_csv('hollys_branches.csv',encoding="utf-8",index=False)


url='https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={}&sido=&gugun=&store='
hollys(url)

