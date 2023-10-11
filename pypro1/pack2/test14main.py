# 사용자 정의 모듈 call
print('뭔가를 하다가... 다른 모듈 호출')

# 같은 패키지 내의 모듈 읽기
import pack2.test14other

print('score : ', pack2.test14other.score)
print(pack2.test14other.__file__)    # __ system이 제공 C:\work\pysou\pypro1\pack2\test14other.py
print(pack2.test14other.__name__)    # pack2.test14other

list1 = [1,2]
list2 = [3,4]
pack2.test14other.listHap(list1, list2)

def abc():
    if __name__ == '__main__':
        print('메인 모듈이야라고 외치다.')
abc()

print()
pack2.test14other.kbs()
from pack2.test14other import kbs, Mbc, score
kbs()
Mbc()
print(score)

# 다른 패키지 내의 모듈 읽기
import moduleTest.test14etc
moduleTest.test14etc.Hap(5, 3)

from moduleTest.test14etc import Cha
Cha(5,3)

import test14etc2
test14etc2.Gop(5, 3)
from test14etc2 import Nanugi
Nanugi(5, 3)



























