# 함수 : 반복소스의 단순화를 목표로, 여러 개의 수행문을 하나의 이름으로 묶은 실행단위
# 내장함수
import math
print(sum([3,4,5]))
print(bin(8))
print(int(1.5), float(3), str(5) + '오')
print(round(1.3),round(1.6))

print(math.ceil(1.3), math.ceil(1.6))   # 올림
print(math.floor(1.3), math.floor(1.6)) # 내림

x =[10,20,30]
y = ['a','b']
for i in zip(x,y):
    print(i)
    # ...

print('----'*10)
# 사용자 정의 함수
# def 함수명(parameter, ...):
#    ...
#    [return<반환값>]

def func1():
    print('func1 수행')
    
    
func1()
print(func1)
print('딴짓 하다가')
imsi = func1()
print(imsi)

print()
def func2(para1, para2):
    result = para1 + para2
    aa = func3(result)
    return aa

print()
def func3(result):
    if result % 2 == 1:
        return 
    else:
        return result
    
print(func2(3,4))
print(func2(3,5))
print(func2,id(func2))

print()
def swap(a,b):
    return b, a

a =10; b = 20

print(swap(a,b))

def func4():
    print('func4 처리')
    def func5():
        print('내부 함수 처리')
    func5()
    
func4()

# if 조건식 안에 함수 사용
def isodd(para):
    return para % 2 == 1

mydict = {x:x*x for x in range(11) if isodd(x)}
print(mydict)