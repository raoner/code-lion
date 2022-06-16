import random


count = int(input('로또 몇 장 필요하세요 : '))

for i in range(count):
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    print(lotto)



