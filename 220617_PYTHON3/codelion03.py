import requests # 사이트에 요청하기 위해, 응답.
import json # json : json is "JavaScript Object Notation"
from bs4 import BeautifulSoup
from pprint import pprint # https://datagy.io/python-pretty-print-dictionary/
# pprint는 딕셔너리 형태를 이쁘게, 구조적으로 출력 해 주는 모듈?이다.


#응용프로그램 프로그래밍 인터페이스 application programming interface. API.
#인터페이스란
#사람 - 키보드.마우스 - 컴퓨터 사이의 것 키보드 마우스.
# 사람과 - 스마트폰 카톡 - 사람 사람과 사람을 연결해주는 중간.. 것.
# 클라이언트(사용자,유저,사람) - API - 서버(대기업, 다음, 카톡)

city = 'Seoul'
apikey = 'c3199d59a9d71fb38f99d057e773956c'
lan = 'kr'

# api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

api = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lan={lan}'
# print(api)
result = requests.get(api)

data = json.loads(result.text)
pprint(data)
# print(type(result.text))

print(data['name'], '의 날씨입니다.')
print('날씨는 ',data['weather'][0]['main'],'입니다.')
print('현재 온도는 ',data['main']['temp'],'입니다.')
print('하지만 체감 온도는 ',data['main']['feels_like'],'입니다.')
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ",data["wind"]["deg"],"입니다.")
print("풍속은 ",data["wind"]["speed"],"입니다.")


'''

city = 'Seoul'
apikey = 'c3199d59a9d71fb38f99d057e773956c'
lang = 'kr'

api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'

result = requests.get(api)
data = json.loads(result.text)

print(data["name"],"의 날씨입니다.")
print("날씨는 ",data["weather"][0]["description"],"입니다.")
print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ",data["wind"]["deg"],"입니다.")
print("풍속은 ",data["wind"]["speed"],"입니다.")

'''