for i in range(30):
    print(i)

foods = ['된장찌개', '피자', '제육볶음']
print(foods[0])
print(foods[1])
print(foods[2])

for i in range(3):
    print(foods[i])

for i in foods:
    print(i)

info = {'고향':'동작구', '취미':'게임', '좋아하는 음식':'고기'}

for i, j in info.items():
    print(i,' : ', j)
