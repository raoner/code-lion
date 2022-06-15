# 내가 직접 짠 소스. / set 집합이 신기방통.. 좋다.
lunch = ['된장찌개', '피자', '제육볶음', '짜장면']

while True:
    print(lunch)
    item = input('음식을 추가 하세요 (q:queit) : ')
    if item == 'q':
        break
    else:
        lunch.append(item)

set_lunch = set(lunch)
print(set_lunch)