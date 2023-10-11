print('tuple ---------------------')
# tuple : list 와 유사하나 읽기 전용 (list 보다 처리 속도가 빠르다) -순서 有, 수정 x 묶음형 자료
# t = ('a','b','c')
t = 'a','b','c'
print(t, type(t), len(t))
print(type(tuple()))
print(t[0])

# t[0] = 'k'   # TypeError: 'tuple' object does not support item assignment
li = list(t)
li[0] = 'k'
t= tuple(li)
print(t, type(t))

# p=(1)  # 1 <class 'int'>
p = (1,)
print(p, type(p))

print('set -----------------------')
# set type : 순서 x, 수정 o, "중복 불가"
a = {1, 2, 3}
print(a, type(a))
print(type(set()))
# print(a[0]) 'set' object is not subscriptable
# a[0] = 10 # 수정 불가(인덱싱이 불가 하므로)

b = {3,4}
print(a.union(b))  #합집합
print(a.intersection(b))  # 교집합
print(a-b, a | b, a & b) # 차,합,교집합

print()
b.update({6,7})  #  원소 추가
b.update((8,9))
b.update([9,10])
print(b)

b.discard(7)    # 값에 의한 삭제
b.remove(8)    # 값에 의한 삭제
b.discard(7)    # 값에 의한 삭제 -  해당 값이 없으면 통과
#b.remove(8)    # 값에 의한 삭제 - 해당 값이 없으면 에러
print(b)

li = ['tom', 'oscar', 'tom']
s = set(li)
li = list(s)
print(li)

print("dict----------------------")
# dict type : 키 값의 형태로 쌍을 이룸. 순서:  x. 키를 이용해 값을 조회
mydic = dict(k1=1, k2='123', k3=3.4)
print(mydic, type(mydic))   # {'k1': 1, 'k2': '123', 'k3': 3.4} <class 'dict'>

dic = {'파이썬': '뱀', '자바':'커피', '스프링':'봄', '숫자':[1,2,3]}
print(dic, type(dic), len(dic))
print(dic['자바'])
#print(dic['커피']) key error
dic['자바'] = '프로그래밍언어' #  해당 키로 값을 수정
print(dic)
dic['오라클'] = '예언자' # 추가
print(dic)
del dic['오라클'] # 삭제
dic.pop('숫자')  # 삭제
print(dic)