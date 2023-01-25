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
print(soup.find('div'))

print(soup.find('div', {'id':'text_id2'}))

div_text = soup.find('div', {'id':'text_id2'})
print(div_text.get_text())

href_link = soup.find('a', {'class':'internal_link'}) # 딕셔너리 형태
# href_link = soup.find('a', class_ ='internal_link') # class는 파이썬 예약어
print(href_link) # <a class'internal_link'…> 태그 전체를 추출
print(href_link['href']) # <a> 태그 내부 href 속성의 값(url)을 추출
print(href_link.get('href')) # ['href']와 동일 기능
print(href_link.text) # <a> Page1 </a>태그 내부의 텍스트(Page1) 추출


print('href_link.attrs: ', href_link.attrs) # <a>태그 내부의 모든 속성 출력
print('values():', href_link.attrs.values()) # 모든 속성들의 값 출력
values = list(href_link.attrs.values()) # dictionary 값들을 리스트로 변경
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))


from bs4 import BeautifulSoup
tr = '''
<table>
<tr class="passed a b c" id="row1 example"><td>t1</td></tr>
<tr class="failed" id="row2"><td>t2</td></tr>
</table>
'''
table = BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr'):
    print(row.attrs)

href_value = soup.find(attrs={'href' : 'www.google.com'})
print(href_value)
print(href_value['href'])
print(href_value.text)


span_tag = soup.find('span')
print('span tag:', span_tag)
print('attrs:', span_tag.attrs) # attribute 속성 추출
print('value:', span_tag.attrs['class']) # class 속성의 값 추출
print('text:', span_tag.text)