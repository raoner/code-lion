# 반복문은 조건문을 포함하니까.
# if <condition:조건>: 부분에 True 또는 False가 되는 코드를 작성합니다.

# if <condition>: 
    # 이곳에 작업할 코드를 입력합니다.

# integer_input = int(input('Enter an integer : '))

# if integer_input%2==0 :
#     print(f'{integer_input} is even')
# else:
#     print(f'{integer_input} is odd')


# user={
#     'username':'namgyu',
#     'password':'kosenrufu'
# }
# count = 0
# success = 0
# while count < 5 and success != 1:
#     username = input('ID : ')
#     password = input('PW : ')
#     if username == user['username'] and password == user['password']:
#         print('Login Success')
#         print('Go Home?')
#         success = 1
#     elif count == 4:
#         print('Account is Locked!')
#     else:
#         print('Login Failed', count+1)
#         print('Try Again')
#         count += 1
#     print('This is out')



    
# True

# select username
#     case user['username']:
# for i in range(2):
#     nation = input('Input a nation : ')
#     capital = 'Unknown'

    # if nation == 'Korea':
    #     capital = 'Seoul'
    # elif nation == 'USA':
    #     capital = 'Washington D.C.'
    # elif nation == 'France':
    #     capital = 'Paris'
    # else:
    #     pass
    # print(f'Capital of {nation} is {capital}')


    # def number_to_string(nation):
    #     match nation:
    #         case 'korea':
    #             capital = 'seoul'
    #         case 'usa':
    #             capital = 'washington d.c.'

# i=0
# while i<5:
#     i+=1
#     print('*'*i)



# user = {
#     "username": "aquashdw",
#     "password": "12345679",
# }

# success = False
# i = 0
# while i < 5 and not success:
#     username = input("input username: ")
#     password = input("input password: ")

#     if user["username"] == username and user["password"] == password:
#         print("Login Success")
#         success = True
#     else:
#         print("Login Failed")
#     i = i + 1

# if not success:
#     print("Account is locked!")


# name_list = ['강남규', '천지영', '김혜진', '김정수']
# name_dict_list = []
# for name in name_list:
#     # print(name)
#     name_dict_list.append({
#         'name':name
#     })

# print(name_dict_list)

# menu_list = ['chicken','pizza','beer']

# for menu in menu_list:
#     print(f'We have {menu}')
#     for char in menu:
#         print(char)

athlete = { # 애슬리트 선수?
    "name": "오진혁",
    "event": "archery",
    "age": 40,
    "height": 182,
    "participated": [
        "2012 London Olympics",
        "2020 Tokyo Olympics",
    ],
    "medals": [
        {
            "games": "2012 London Olympics",
            "event": "archery",
            "competition": "men individual",
            "medal": "gold"
        },
        {
            "games": "2012 London Olympics",
            "event": "archery",
            "competition": "men's team",
            "medal": "bronze"
        },
        {
            "games": "2020 Tokyo Olympics",
            "event": "archery",
            "competition": "men's team",
            "medal": "gold"
        }
    ],
}
# for key in athlete.keys():
#     print(athlete.get(key))

# for value in athlete.values():
    # print(value)

# key:value
# name: 오진혁
# event:archery

# for key in athlete.keys():
#     print(f'{key}:{athlete.get(key)}')

# for key, value in athlete.items():
#     print(f'{key}:{value}')



# for i in range(1,11):
#     print(i)

# i=1
# while i<11:
#     print(i)
#     i+=1

# # for medal,i in athlete_medals,range(len(athlete_medals)):
#     print(f'{i+1}:{medal.get('medal')}')

# athlete_medals = athlete.get("medals")

# for idx, medal in enumerate(athlete_medals):
#     print(f"{idx + 1}: {medal.get('medal')}")

# password = 'password'
# while True:
#     input_password = input('PASSWORD : ')
#     if input_password == password:
#         print('Login Success!')
#         break
#     print('Incorrect!')
#     print('Try again')
# print('Hello!')

# people = [
#     {'vaccinated':True},
#     {'vaccinated':False},
#     {'vaccinated':True},
#     {'vaccinated':False},
#     {'vaccinated':True},
#     {'vaccinated':False},
#     {'vaccinated':True},
#     {'vaccinated':True},
# ]
# group_count = 0
# for person in people:
#     # if person['vaccinated']:
#     #     continue
#     # group_count += 1
#     if not person['vaccinated']:
#         group_count += 1

# print(group_count)