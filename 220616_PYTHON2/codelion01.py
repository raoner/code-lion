
# step 01
# name = input('이름을 입력해주세요 : ')
# print(name + '씨 안녕하세요!')

# step 02
# food1 = int(input('내가 먹은 음식의 가격 : '))
# food2 = int(input('친구가 먹은 음식의 가격 : '))
# print(food1 + food2)

# step03
# 월세 = input('월세를 입력해주세요 : ')
# 관리비 = input('관리비를 입력해주세요 : ')
# 찐월세 = int(월세) + int(관리비)
# print(찐월세)

# step04, 05(list method append, insert)
# orders = ['짜장', '짬뽕', '탕수육']
# orders.append('냉면')
# orders.insert(1, '초밥')
# orders.insert(3, '양장피')
# print(orders)

# step06, 07
# (commend del: Access the address of the variable and delete the value, 
# method remove: remove into a value)
# orders = ['짜장', '짬뽕', '탕수육']
#del orders[0] == orders.remove('짜장')
# print(orders)
# print(len(orders))

# # step08
# num = [20,40,50,10,30]
# # sum method 01 : 내가 한 것
# sum = 0
# for i in num:
#     sum = sum + i
# print(sum)
# # sum method 02
# sum = 0
# sum = sum(num)
# print(sum)

# # step09
# num = [20,40,50,10,30]
# # # avg method 01 : 내가 한 것
# avg = sum(num) / len(num)
# print(avg)

# step10 dictionery
family = {'아빠':39,
        '엄마':34,
        '아이':0
        }
print(family['아이']+1)

family['둘째'] = 0

print(family['둘째'], family['엄마'])

family['아이'] = 2
print(family['아이'])
print(family)

del family['둘째']
print(family)
