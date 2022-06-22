from matplotlib.pyplot import title
import requests
# from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
# import bs4

# print(requests.get)

# put, get post delete, 요청하면 응답. 예)배가고파져서 주문이요. 햄버거 , 주문받았습니다. 요리해서 햄버거 돌려줌.
# server 응답 / client 요청하면 /
# url = 'https://lifena.netlify.app/'
url = 'https://sports.daum.net/photocenter'
response = requests.get(url)
# print(type(response.text[:500]))
# print((response.text[:500]))
# print((response.text))


#패키지에서 뷰티플 모듈을 쓰겠다.

# 프롬이 패키지를 참조하고, 뷰티플은 쓰겠다...
# print(type(BeautifulSoup(response.text, 'html.parser')))

soup = BeautifulSoup(response.text, 'html.parser')
# str(BeautifulSoup(response.text,'html.parser'))
# file = open("daum.html","w")
# file.write(soup)
# file.close()

# a tag, class text_pctop* class ir_wa


results = soup.findAll('a','link_info')
sport_tail_list = open('sport_tail_list.txt','a')

title = str(datetime.today().strftime('오늘은 %y년 %m월 %d일이며, \ndaum 스포츠의 홈의 하단의 하이퍼텍스트의 스트링 목록들 입니다.'))
print('\n'+ title + '\n')
sport_tail_list.write(title+'\n\n')

numbers = 1
for result in results:
    data = str(numbers) + '. ' + result.get_text()
    sport_tail_list.write(data + '\n')
    print(data)
    numbers += 1
print('\n')
# print(soup.findAll('a','link_info'))
# print(soup.findAll('div','d_index'))
# print(str(soup.findAll('html')[0])[:20])

# print(soup.title)
# print(soup.title.string)
# print(soup.findAll('meta'))
# print(soup.h3.string)
# 데이터와 파싱방법 html, xml올 수 있다. 리퀘스트로 텍스트 데이터로 되었고, 파싱방법 우리의 문서 데이터를 의미있게 변경하는 방법 / 
# 어떤 문장 문자를 의미가 있는 데이터로 바꾸는거.. 파써 기본 파서를 html.parser 파이썬에서 기본 제공하는 것.



# print(response)

# print(response.text)

# print(response.url)

# print(response.content)

# print(response.encoding)

# print(response.headers)

# print(response.json)

# print(response.links)

# print(response.ok)

# print(response.status_code)

#server return : requests.response