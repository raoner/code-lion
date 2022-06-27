from inspect import Parameter
from operator import is_


def print_hello_world():
    print('hello, world!')

print_hello_world()


def say_hello(name):
    new_name = name
    small_case_name = name.lower()
    print(f"hello, {name}!")

say_hello("Namgyu")
say_hello("김종수")
say_hello("김고은")
say_hello("조재혁")
say_hello("정수")


def calculate_age(name, year):
    print(f"hello, {name}! you are {2021 - year + 1}s old.")

calculate_age("namgyu", 39)

def read_athlete_data(athlete):
    if not isinstance(athlete, dict):
        print("wrong input")
    else:
        print("ead athlete data")
        # dict.get()
        return athlete.get("name")


        # print(athlete["name"])
        # print(athlete["age"])
        # print(athlete["event"])
        # print(athlete["nationality"])

athlete_oh = {
    "name":"namgyu",
    "age":39,
    # "event":
    # "nationality":
}

# read_athlete_data(athlete_oh)

# input("계속하려면 엔터를 누르세요...")

def is_leap_year(year):
    result = False
    if year % 4 == 0:
        # 그래고리력.? 4의 배수 100의 배수, 100의 배수이면서 4의 배수도 윤년이 아니다.
        if year % 100 == 0 and year % 400 != 0 :
            # result = False
            pass
        else:
            result = True
    else:
        # result = False
        pass
    return result

print(is_leap_year(2016))
print(is_leap_year(2100))
print(is_leap_year(2020))

# list 사람 받고 몇명 이상을 모였는지를 인자를 받고 기준을 받고
# 안맞은 사람이 그 사람이 이상이면?.. 사회적 기준..
# 이사람들은 모일 수 있냐?는 함수
def can_group(limit, people):
    print(is_leap_year)
    if not isinstance(people, list):
        return False
    group_count = 0
    for person in people:
        if not isinstance(person, dict):
            group_count = group_count + 1
            continue
        if "vaccinated" in person.keys() and person.get("vaccinated"):
            continue
        else:
            group_count = group_count + 1
    return group_count < limit

people = [
    {'vaccinated':True},
    {'vaccinated':False},
    {'vaccinated':True},
    {'vaccinated':False},
    {'vaccinated':True},
    {'vaccinated':False},
    {'vaccinated':True},
    {'vaccinated':True},
]

print(can_group(10,people))
                
# 팩토리얼 피보나치, 재귀함수.

# print(can_group(10,12 ))

def calculate_age(name, born_year, current_year=2022):
# def calculate_age(name="Doe", born_year=, current_year=2022):
# 두개를 어디다 넣어줘야 할 것이 명확하게 해석할 수 없게 되어.. 
    print(f"Hello {name}! You are {current_year - born_year + 1} year old.")


calculate_age("namgyu", 40)
calculate_age("namgyu", 20,2021)

def create_car(name, brand="현대", engine="휘발유", passengers=5,):
    return {
        "name":name,
        "brand":brand,
        "dngine":engine,

    }


