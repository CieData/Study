from urllib.request import urlopen
from bs4 import BeautifulSoup
html='https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Y9DUAnZBy3A'
def scraping_use_find(html):
    html = urlopen(html)
    soup = BeautifulSoup(html.read(), 'html.parser')
    li_tags = soup.find_all('li', {'class' : 'forecast-tombstone'})
    image = soup.find_all('img',{'class' : 'forecast-icon'})
    
    print('[find 함수 사용]')
    print(f'총 tomestone-container 검색 개수 : {len(li_tags)}')
    print('---------------------------------------------------------------------------')

    for i in range(len(li_tags)):
        print('[Period] :',li_tags[i].find_all('p')[0].text)
        print(f'[Short desc] :',li_tags[i].find_all('p')[2].text)
        print(f'[Temperature] :',li_tags[i].find_all('p')[3].text)
        print(f'[[Image	desc] : {image[i].title}')
        print('---------------------------------------------------------------------------')

def scraping_use_select(html):
    html = urlopen(html)
    soup = BeautifulSoup(html.read(), 'html.parser')
    li_tags = soup.select('li.forecast-tombstone')
    image = soup.select('img.forecast-icon')
    
    print('[select 함수 사용]')
    print(f'총 tomestone-container 검색 개수 : {len(li_tags)}')
    print('---------------------------------------------------------------------------')

    for i in range(len(li_tags)):
        print('[Period] :',li_tags[0].select('p')[0].text)
        print(f'[Short desc] :',li_tags[0].select('p')[2].text)
        print(f'[Temperature] :',li_tags[0].select('p')[3].text)
        print(f'[[Image	desc] : {image[i].title}')
        print('---------------------------------------------------------------------------')