# 자료형
# int, float, boolean, complex : 객체 값 하나를 참조. Immutable 객체
# list, tuple, set, dict : 묶음형 객체 값 참조. 

# str : 문자열 자료형 : 순서 有 - 인덱싱,슬라이싱 가능, 변경 불가 
s = 'sequence'
# 문자열 관련 함수 
print(len(s))
print('포함 횟수: ', s.count('e'))
print('검색 위치: ', s.find('e'), s.find('e',3), s.rfind('e'))
#...

ss = 'mbc'
print('mbc', ss, id(ss))  # id함수 
ss = 'abc' # Immutable 객체
print('mbc', ss, id(ss))

print(s, s[0], s[-7]) # 인덱싱
print(s, s[0:5], s[-7:-5], s[5:], s[:5],  s[::2], s[0:7:3]) # 슬라이싱
print(s[0:5] + 'good')
print()
sss =  '  mbc kbs sbs  '
print(sss)
print(ss.strip())
print(ss.lstrip())
print(ss.rstrip())
ssss= sss.split(sep='   ')
print(ssss)
s5 = sss.replace('kbs', '공영방송')
print(s5)

print("\n\nList ---------------------")
# list : 배열과 유사. 중복 자료 허용, 여러 종류의 값 기억. 순서 有, 변경 o
a = [1, 2, 3]
print(a, type(a))
b = [10, a, 12.3, 'good', False]
print(b)
c = list();
print(c, type(c))
print()
family = [ '준수', '예진', '정혜']
family.append('준호')
family.insert(0, '민규')
family.extend(['tom',' oscar'])
family += ['지원', '국인']
family.remove('tom')
# family.clear()
print(family, len(family), family[0])

print()
aa= [1,2,3,['a','b', 'kbs'],4,5]    # 중첩리스트
print(aa, aa[0], aa[0:3])
print(aa[3], '  ', aa[3][2])
aa.remove(2)  # 값에 의한 삭제
del aa[3]       # 순서에 의한 삭제
print(aa)

print()
bb = aa         # 주소 치환 : 같은 객체를 참조. 얕은 복사
print(aa, ' ', bb, id(aa), id(bb))
bb[0] = 'nice'
print(aa, ' ', bb)

import copy
cc = copy.deepcopy(aa)   # 주소 치환 : 새로운 공간이 확보 깊은 복사
print(aa, ' ', cc, id(aa), id(cc))
print(aa ==cc, aa is cc)
cc[0] = '쉬고할까'
print(aa, ' ', cc)

print('자료구조 : stack, queue')
sbs= [10,20,30]
sbs.append(40)
print(sbs)
sbs.pop()       # stack구조 LiFO처리
print(sbs)
sbs.pop()
print(sbs)
print('\n')
sbs= [10,20,30]
sbs.append(40)
print(sbs)
sbs.pop(0)       # queue구조 FiFO처리
print(sbs)
sbs.pop(0)
print(sbs)
