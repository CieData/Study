# 임의의 위키 페이지에서 모든 링크 목록 가져오기
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.parse import quote
from bs4 import BeautifulSoup
import datetime
import random
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


#random.seed(datetime.datetime.now())
#링크간 무작위 이동하기 : 소스 코드
random.seed(None) # Python 3.9 이상
def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    bodyContent = bs.find('div', {'id': 'bodyContent'})	
    wikiUrl = bodyContent.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))	
    return wikiUrl

links = getLinks('/wiki/Kevin_Bacon')
print('links 길이: ', len(links))
while(len(links)) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

#같은 페이지를 두 번 크롤링 하지 않기

pages = set() # 세트 선언
count = 0
def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새로운 페이지 발견
                newPage = link.attrs['href']

                count += 1
                print('[{0}]: {1}'.format(count, newPage))
                pages.add(newPage)
                getLinks(newPage)
getLinks('')


urlString1 = 'https://shopping.naver.com/home/p/index.naver'
url = urlparse(urlString1)
print(url.scheme)
print(url.netloc)
print(url.path)

'''
Web Scraping with Python
3장. 크롤링 시작하기
- 여섯 다리의 법칙
https://namu.wiki/w/6단계%20법칙

'''
# 예제 5


pages = set()
count = 0
def getLinks(pageUrl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text()) # <h1>태그 검색 
        #print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find(id='mw-content-text').find('p').text)
        # 편집 버튼: <li id="ca-edit"> 태그에 존재 
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError as e:
        print('this page is missing something! Continuing: ', e)

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-'*40)
                count += 1
                print('[{0}]: {1}'.format(count, newPage))
                pages.add(newPage)
                getLinks(newPage)

getLinks('')



'''
3.3 인터넷 크롤링

예제 6
'''

random.seed(None)
# 웹 페이지에서 발견된 내부 링크를 모두 목록으로 만듬
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    # "/"로 시작하는 링크를 모두 찾음
    for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


# 웹 페이지에서 발견된 외부 링크를 모두 목록으로 만듬
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # 현재 URL을 포함하지 않으면서 http나 www로 시작하는 
    # 링크를 모두 찾음
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    try:
        html = urlopen(startingPage)
        bs = BeautifulSoup(html, 'html.parser')
        externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    
        if len(externalLinks) == 0: # 외부 링크가 없으면 내부 링크 검색
            print('No external links, looking around the site for one')
            domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
            print('domain: ', domain)
            internalLinks = getInternalLinks(bs, domain)
            return getRandomExternalLink(internalLinks[random.randint(0,
                                                                  len(internalLinks) - 1)])
        else: # 랜덤하게 외부 링크 선택                
            return externalLinks[random.randint(0, len(externalLinks) - 1)]
    except Exception as e:
        print('Exception 발생: ', e) 

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    # quote(externalLink): 한글이 포함된 url인 경우, UnicodeEncodeError 발생
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com')



'''
3.3 인터넷 크롤링

예제 7
'''

# 웹 페이지에서 발견된 내부 링크를 모두 목록으로 만듬
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    # "/"로 시작하는 링크를 모두 찾음"
    for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


# 웹 페이지에서 발견된 외부 링크를 모두 목록으로 만듬
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # 현재 URL을 포함하지 않으면서 http나 www로 시작하는 링크를 모두 찾음
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

# 사이트에서 찾은 외부 URL을 모두 리스트로 수집 
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
                              urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)

allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')