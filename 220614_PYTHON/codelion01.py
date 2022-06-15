'''한국말을 러시아말로 하는데,
LIST TYPE으로 목록 나열 - 첫번째 된장찌개 피자 제육볶음 제일 안에 넣고
random.choice method로 한개의 값 리턴 - 두번째 인형은 랜덤으로 뽑고
cli에서 목록을 화면으로 출력 - 세번째 인형은 랜덤으로 하나를 출력하자'''

import random
import time

#for i in range(5):
i = 0
while True:
    print(random.choice(['된장찌개', '피자', '제육복음', '치킨', '떡볶이']))
    time.sleep(1)
    i = i + 1
    if i > 5:
        break


