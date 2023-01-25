'''
§ select_one()과 find() 차이점
• find()
    하위 태그를 찾을 때, 반복적으로 코드를 작성
    soup.find('div').find('p')
• select()
    하위 태그를 찾을 때, 직접 하위 경로 지정
    soup.select_one('div > p')
'''
html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>
        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="external_link" href="www.naver.com">naver</a>
            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head.text)
print(head.text.strip())

h1 = soup.select_one('h1') # 첫 번째 <h1>태그 선택
print(h1)

# <h1>태그의 id가 "footer＂인 항목 추출
footer = soup.select_one('h1#footer')
print(footer)

class_link = soup.select_one('a.internal_link')
print(class_link)

print(class_link.text)
print(class_link['href'])

# 계층적 접근
link1 = soup.select_one('div#link > a.external_link')
print(link1)

#find 함수와 비교
link_find = soup.find('div', {'id': 'link'})
external_link = link_find.find('a', {'class': 'external_link'})
print('find	external_link: ', external_link)

#(상위태그 하위태그) 형식으로 접근
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.text)

#모든 <h1>태그 검색
h1_all = soup.select('h1')
print(h1_all)

#모든 url 링크 검색
# html문서의 모든 <a> 태그의 href 값 추출
url_links = soup.select('a')
for link in url_links:
    print(link['href'])
    
#<div id=“class1”> 내부의 모든 url 검색
div_urls = soup.select('div#class1 > a')
print(div_urls)
print(div_urls[0]['href'])

# <h1 id="heading”>과 <h1 id="footer”> 항목 가져오기
h1 = soup.select('#heading, #footer')
print(h1)

url_links = soup.select('a.external_link, a.internal_link')
print(url_links)


national_anthem = '''
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>애국가</title>
</head>
<body>
   <div>
       <p id="title">애국가</p>
       <p class="content">
           동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
           무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
       </p>
       <p class="content">
           남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세.<br>
           무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
       </p>
       <p class="content">
           가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
           무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
       </p>
       <p class="content">
           이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
           무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
       </p>               
   </div>
</body>
</html>
'''

soup = BeautifulSoup(national_anthem, 'html.parser')
print(soup.select_one('p#title').text)

contents = soup.select('p.content')
for content in contents:
    print(content.text)

