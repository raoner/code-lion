from secrets import choice


menu1 = set(['된장찌게', '피자', '제육볶음'])
menu2 = set(['된장찌게', '떡국', '김밥'])

# menu3 = menu1 | menu2 # | : 파이푸 심볼 겹친거는 제외하고 모두 출력
# menu3 = menu1 & menu2 # 교집합 겹치는 메뉴만 출력
menu3 = menu1 - menu2 # 차집합 겹치는 메뉴를 첫번째 메뉴에서 빼는 것
print(menu3)

