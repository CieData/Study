# 임의의 위키 페이지에서 모든 링크 목록 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])


#• 정규식: ^(/wiki/)((?!:).)*$
# ^: 정규식 시작, $: 정규식 끝
# (/wiki/): ‘/wiki/’ 문자열 포함
# ((?!:).)*: ‘:’이 없는 문자열 및 임의의 문자가 0회 이상 반복되는 문자열 검색 (전방부정탐색)
body_content = bs.find('div', {'id': 'bodyContent'})
pattern = '^(/wiki/)((?!:).)*$'
for link in body_content.find_all('a', href=re.compile(pattern)):
    if 'href' in link.attrs:
        print(link.attrs['href'])