# athlete_oh={
#     'name':'오진혁',
#     'event':'archery'

# }

# name_key = 'name'
# print(athlete_oh[name_key])

# event_key = 'event'
# print(athlete_oh[event_key])

# age_key = 'age'
# print(athlete_oh.get(age_key))
# athlete_oh[age_key] = 40
# print(athlete_oh[age_key])
# athlete_oh['height'] = 182
# athlete_oh[name_key] = 'Oh Jinhyek'

# print(athlete_oh)

# # get update pop keys
# athlete_oh.update({
#     'birth':'1981-08-15',
#     age_key:41,
#     'medals':['Gold','Gold','Gold']
# })

# print(athlete_oh)
# print(athlete_oh.pop('medals'))

# print(athlete_oh.keys())
# print(athlete_oh.values())
# print(athlete_oh.items())

# print(type(athlete_oh[age_key]))


# print(list(athlete_oh.items()))

# athlete = { # 애슬리트 선수?
#     "name": "오진혁",
#     "event": "archery",
#     "age": 40,
#     "height": 182,
#     "participated": [
#         "2012 London Olympics",
#         "2020 Tokyo Olympics",
#     ],
#     "medals": [
#         {
#             "games": "2012 London Olympics",
#             "event": "archery",
#             "competition": "men individual",
#             "medal": "gold"
#         },
#         {
#             "games": "2012 London Olympics",
#             "event": "archery",
#             "competition": "men's team",
#             "medal": "bronze"
#         },
#         {
#             "games": "2020 Tokyo Olympics",
#             "event": "archery",
#             "competition": "men's team",
#             "medal": "gold"
#         }
#     ],
# }

# print(athlete['medals'][0]['medal'])

# tuple 공구함?!
# 소괄호 아이템들이 콤마로 구분되면 튜플 tuple

a = 1,
print(a*10)

# 위치가 고정이 되고, 상자의 크기를 바꿀 순 없음. 데이터를 하나의 묶음으로 보관, 구분자로써 ,가 들어가는 튜플의 상태로 인식됨.

a = 1, 2, 3
b,c,d = a
print(a)
print(a,b,c,d)

# 튜플을 넣으려면, 리스트로 해서, 