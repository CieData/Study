from bs4 import BeautifulSoup
from urllib.request import urlopen

#css 속성을 이용한 검색
html_text='<span class="red">Heavens! what a virulent attack!</span>'
soup = BeautifulSoup(html_text, 'html.parser')
object_tag = soup.find('span')
print('object_tag:', object_tag)
print('attrs:', object_tag.attrs)
print('value:', object_tag.attrs['class'])
print('text:', object_tag.text)


html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, "html.parser")
# 등장인물의 이름: 녹색
nameList = soup.find_all('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())


#특정 단어 찾기
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')
princeList = soup.find_all(text='the prince')
print(princeList)
print('the prince count: ', len(princeList))


#트리 이동 : 자식과 자손
#자식 : children
#자손 : descendants
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')
table_tag = soup.find('table', {'id':'giftList'})
for child in table_tag.children:
    print(child)

desc = soup.find('table', {'id':'giftList'}).descendants
print('descendants 개수: ', len(list(desc)))

for child in soup.find('table', {'id':'giftList'}).descendants:
    print(child)

#트리 이동 : 형제 다루기
#형제 : next_siblings, previous_siblings
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')
for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)	

for sibling in soup.find('tr', {'id':'gift2'}).previous_siblings:
    print(sibling)

#트리 이동 : 부모 다루기
#부모 : parent
style_tag = soup.style
print(style_tag.parent)

img1 = soup.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)
