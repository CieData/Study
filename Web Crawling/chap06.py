'''
6장. 데이터 저장
 6.1 미디어 파일

'''
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
print(type(html))
print(type(html.read()))
bs = BeautifulSoup(html, 'html.parser') # object형태를 BeautifulSoup에 전달
# bs = BeautifulSoup(html.read(), 'html.parser') # 문자열 형태를 전달

home_image = bs.find('img', {'class':'pagelayer-img'})
image_location = home_image['src']
print(image_location)
urlretrieve(image_location, 'logo.jpg')


downloadList = bs.find_all(src=True)

for down_url in downloadList:
    print(down_url['src'])


'''
    6.1 내부 파일 저장 
'''

downloadDirectory = 'downloaded'
baseUrl = 'https://pythonscraping.com'

def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:]) # 인덱스 11부터 끝까지
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://{}'.format(source)
    else:
        #url = '{}/{}'.format(baseUrl, source)
        url = '{}'.format(source)    
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen('https://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.find_all('img', src=True)
#downloadList = bs.find_all('img')


for download in downloadList:            
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
