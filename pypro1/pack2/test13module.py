# Module : 소스 코드의 재 사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 관리하여 저장하면 '.py'로 저장된다.
# module은 package 내에 있어야 한다. 
# 표준 모듈, 사용자 정의 모듈, 제 3자(third party) 모듈로 구분할 수 있다. 

# 내장된 모듈은 별도의 작업 없이 사용
print('모듈의 멤버 : 명령문, 함수, 클래스, 모듈')
# 설치는 되었으나 loading 되지 않은 모듈(외부 모듈)은 import 키워드로 로딩 후 사용한다. 
import sys
print(sys.path)
# sys.exit()  # 프로그램의 강제 종료
# print('프로그램 종료')

print(sum([1,2,3]))

import math 
print(math.e, ' ', math.pi)
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6)   # 일요일을 첫 요일로 지정
calendar.prmonth(2023, 10)

import numpy
print(numpy.abs(-3))

import random
print(random.random())
print(random.randrange(1, 10))

from random import random
# from random import * -> 비권장 
print(random())  # import random print(random.random()) 와 동일함
 
