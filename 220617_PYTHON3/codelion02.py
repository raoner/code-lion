from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 우리는 로봇이 아니다. / 이러한 환경이다.
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

url = 'https://sports.daum.net/photocenter'
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.findAll('a','link_info')
sport_tail_list = open('sport_tail_list.txt','w')

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