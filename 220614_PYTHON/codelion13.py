import random
import time

lunch = ['된장찌개', '피자', '제육볶음', '짜장면']

while True:
    print(lunch)
    item = input('음식을 추가 하세요 : ')
    if item == 'q':
        break
    else:
        lunch.append(item)
print(lunch)


set_lunch = set(lunch)
print('모든 음식 목록 : ', set_lunch)
while True:    
    item = input('음식을 삭제 해 주세요 :')
    if item == 'q':
        break
    else:
        set_lunch = set_lunch - set([item])
    print(set_lunch)

print('최종 단계 : ', set_lunch, "중에서 선택 합니다.")

for i in range(5):
    print(5-i)
    time.sleep(1)

print(random.choice(list(set_lunch)))