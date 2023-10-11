# 정규 표현식
import re
from anaconda_project.internal.conda_api import result

ss = "1234 abc가나다 abcABC_1235555_6python is fun만세"
print(ss)
print(re.findall(r'123', ss))
print(re.findall(r' 가나', ss))

print(re.findall(r'[1,2,5]', ss))
print(re.findall(r'[1,2,5]+', ss))   # 반복 관련 메타문자 +: 1회 이상 
print(re.findall(r'[0-9]', ss))       # 문자 집합 []
print(re.findall(r'[^0-9]', ss))       # 문자 집합 [^]  부정
print(re.findall(r'\d+', ss))           # 특수문자 \d-> 숫자만 도출 \D-> 문자만 도출
print(re.findall(r'\D+', ss))
print(re.findall(r'[0-9]{2}', ss))
print(re.findall(r'[0-9]{2,3}', ss))  # {n} n회
print(re.findall(r'[가-힣,a-z,A-Z]+', ss))
print(re.findall(r'^1234', ss))   # 문자열 시작
print(re.findall(r'만세$', ss))     # 문자열 끝

print()
ss= '''
<a href="abc1.html">abc1</a>
<a href="abc2.html">abc2</a>
<a href="abc3.html">abc3</a>
'''
print(ss)
result = re.findall(r'href="(.*)"',ss )       # " ' "" '"
print(result)

print()
p = re.compile('the', re.IGNORECASE)    # flag 사용하기
print(p.findall('The dog the dog'))

s = """My name is tom
I am happy"""
print(s)
p = re.compile('^.+', re.MULTILINE)
print(p.findall(s))



