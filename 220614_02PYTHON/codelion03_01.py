
{'질문':'취미는 무엇입니까','답변':'영화 보기입니다'}

{'취미는 무엇입니까':'영화 보기입니다', '특기는 무엇입니까':'댄스입니다'}

total_dictionary = {}

while True:
    question = input('질문을 입력하세요 : ')
    if question == 'q':
        break
    else:
        total_dictionary[question] = ''

for i in total_dictionary:
    print(i)
    answer = input('답변을 입력 해 주세요 : ')
    total_dictionary[i] = answer
    
print(total_dictionary)
    