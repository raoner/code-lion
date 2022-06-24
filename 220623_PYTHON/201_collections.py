print('Hello, World!')

name_1 = '강대영'
gender_1 = 'male'
major_1 = 'marketing'

name_2 = '이준석'
gender_2 = 'male'
major_2 = 'spanish'

name_list = ['강남규', '천지영', name_1, name_2]

print(name_list[0], len(name_list))

for name in name_list:
    print(name, end='')

name_list[3] = '이종석'

print('\n')
print(name_list)

name_list[3] = '이종석'
print(name_list[0][0])

print('hello world'[0:7])
print('hello world'[:7])
print('hello world'[3:])
print(name_list[0:2])


name_list.append('김정수')
name_list.append('정하림')
print(name_list)

name_list.extend(['문한결','임민정']) # 2개의 노드의 이상을 추가 해준다.
print(name_list)

name_list.append(['장한솔','이준호'])
print(name_list)

print(name_list.pop())
print(name_list)

print(name_list.pop(3))
print(name_list)

print(name_list.remove('김정수'))
print(name_list)

print(name_list.index('천지영'))

print(name_list.sort())
print(name_list)

# sort()는 같은 형끼리만 된다.
