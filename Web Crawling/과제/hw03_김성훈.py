from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

def cate(li,count):
    print('-'*30)
    print(f'[네이버 코스피 상위 {count}대 기업 목록 ]')
    print('-'*30)
    for i in range(count):
        print(f'[{i+1}] {li[i].text}')
def pinance(url,count):
    original_html = requests.get(url)
    soup = BeautifulSoup(original_html.text, "html.parser")
    cat=soup.find_all('a', href=re.compile('/item/main.naver'))
    cat=cat[:count]
    cate(cat,count)
    while True:
        s=int(input('주가를 검색할 기업의 번호를 입력하세요(-1 : 종료): '))
        if s==-1:
            break
        url='https://finance.naver.com/'+cat[s-1].attrs['href']
        original_html = requests.get(url)
        soup = BeautifulSoup(original_html.text, "html.parser")
        code=soup.select('span.code')
        today=soup.select('em.no_up')
        yes=soup.select('td.first')
        yester=yes[0].select('span.blind')
        low=soup.find('span',{'class': 'sptxt sp_txt5'}).parent.select('span.blind')
        print(url)
        print(f'종목명 : {cat[s-1]}')
        print(f'종목코드 : {code[0].text}')
        print(f'현재가 : {today[0].span.text}')
        print(f'전일가 : {yester[0].text}')
        print(f'시가 : {today[4].span.text}')
        print(f'고가 : {today[3].span.text}')
        print(f'저가 : {low[0].text}')
url='https://finance.naver.com/sise/sise_market_sum.naver'
pinance(url,10)
        
        
    




