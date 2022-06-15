
from multiprocessing.dummy import current_process


def make_dolcelatte():
    print('1. 얼음을 넣는다.')
    print('2. 연유를 30ml 넣는다.')
    print('3. 찬 우유를 넣는다.')
    print('4. 에스프로소 샷을 넣는다.')

def make_blueberry_smoothie():
    print('1. 블루베리 20g을 넣는다.')
    print('2. 우유를 300ml 넣는다. ')
    print('3. 얼음을 넣는다.')
    print('4. 믹서기에 간다.')

def make_simple_latte():
    print('1. 커피를 넣는다.')
    print('2. 우유를 넣는다. ')
    print('3. 신나게 섞는다.')


make = input('어떤 음료를 만들 건가요? : ')
scup = input(make, '를 몇잔 만들 건가요? : ')
 
make_simple_latte()
make_blueberry_smoothie()
make_dolcelatte()