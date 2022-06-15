lunch = ['된장찌개','피자','제육볶음','짜장면']
# lunch.append('돈까스')

while True:
    print(lunch)
    item = input('음식을 추가 하시오(q:QUEIT) : ')
    if item == 'q':
        break
    else:
        lunch.append(item)
    
print(lunch)
set_lunch = set(lunch)
