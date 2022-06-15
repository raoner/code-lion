info = {'고향':'남양주', '취미' : '스타2', "좋아하는 음식" : "고기" }
foods = ['된장찌개', '피자', '제육볶음']

print(info.get('취미'))

info['특기'] = '피아노'
info['사는곳'] = '서울'
del info['좋아하는 음식']
print(info)
print(len(info))
info.clear()
print(info)

print(foods[-1])

foods.append('김밥')
print(foods)
foods.clear()
print(foods)