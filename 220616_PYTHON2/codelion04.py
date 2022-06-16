# listSib = [10,20,30]

# for i in listSib: # 시퀀스..?
#     print(i)

#### range(option:(start num), end num, option:(step))
sum = 0
cnt = 0
for i in range(9,1,-3):
    print('안녕하세요.', i)
    sum = sum + i
    cnt = cnt + 1

avg = sum / cnt

print(sum, avg, cnt)

