from bs4 import BeautifulSoup
import requests

url='https://search.naver.com/search.naver?query=대구+날씨'
def naver_weather(url):
    original_html = requests.get(url)
    soup = BeautifulSoup(original_html.text, "html.parser")
    location=soup.select('h2.title')
    temp=soup.select('div.temperature_text')
    weather=soup.select('span.weather.before_slash')
    chart=soup.select('ul.today_chart_list')
    graph=soup.select('dl.graph_content')
    print(f'현재 위치 : {location[0].text}')
    print(f'현재 온도 : {temp[0].text}')
    print(f'날씨 상태 : {weather[0].text}')
    print(f'미세먼지 :',chart[0].select('span.txt')[0].text)
    print(f'초미세 먼지 :',chart[0].select('span.txt')[1].text)
    print(f'자외선 :',chart[0].select('span.txt')[2].text)
    print(f'일출 :',chart[0].select('span.txt')[3].text)
    print('------------------------------')
    print('시간대별 날씨 및 온도')
    print('------------------------------')
    for i in range(len(graph)):
        print(graph[i].select('dt')[0].text,graph[i].select('dd.weather_box')[0].text,graph[i].select('dd.degree_point')[0].text)
naver_weather(url)