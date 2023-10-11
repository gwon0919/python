# 변수의 생존 범위 : global, local
# Local > Enclosing function > Global > Builtin


player = '국가대표'  # 전역변수 (모듈의 어디서든 공유 가능)

def funcSports():
    name = '신기루'    # 지역변수(함수 내에서만 유효)
    player = '지역대표'
    print(name, player)

funcSports()

print()
a=1; b=2; c=3
print('출력1 -- a:{}, b:{}, c:{}'.format(a,b,c))
def outerfunc():
    a=4
    b=5
    def innerfunc():
        global c  # 지역변수가 전역변수로 전환
        nonlocal b
        # c=6
        print('출력2 -- a:{}, b:{}, c:{}'.format(a,b,c))
        c=6
        b=7
    innerfunc()
    print('출력3 -- a:{}, b:{}, c:{}'.format(a,b,c))
outerfunc()
print('출력4 -- a:{}, b:{}, c:{}'.format(a,b,c))

print('\n인수와 매개변수 키워드 매칭------')
def showGugu(start, end=5):
    for dan in range(start, end + 1):
        print(str(dan)+ '단 출력',  end =" ")
        print()
        
showGugu(2, 3)
# showGugu(2)
# showGugu(2,3,4)
showGugu(2) #기본값 매개변수
showGugu(start=2, end=3) # 키워드 매개변수
showGugu(end=3,start=2)
showGugu(2,end=4) 
# showGugu(start=2, 4) # SyntaxError: positional argument follows keyword argument
# showGugu(end=3,2)  #SyntaxError: positional argument follows keyword argumen


# 가변 매개변수
*a,b = [1,2,3,4,5]
def fu1(*ar):  # 파라미터에 패키지 연산자 부여
    print(ar)
    for a in ar:
        print('밥:' + a)
    
fu1('공기밥','주먹밥') # 튜플타입으로 출력
fu1('공기밥','주먹밥','김밥')

def fu2(bap, *ar): # 뒤에다 '*'부여해야함
    print(bap)
    print(ar)
    for a in ar:
        print('밥: ' + a)
        
fu2('공기밥','주먹밥')
fu2('공기밥','주먹밥','김밥')

print()
def selectCalc(choice, *ar):
    if choice == '+':
        imsi = 0
        for i in ar:
            imsi += i
    elif choice == '*':
        imsi = 1
        for i in ar:
            imsi *= i
    return imsi

    
print(selectCalc('+', 1,2,3,4,5))   # tuple 자료
print(selectCalc('*', 1,2,3,4,5))

# dict를 인수로 전달
def fu3(w, h, **etc):  # '**'로 인해 dict 로 받을 수 있다
    print('몸무게:{}, 키:{}'.format(w,h))
    print(etc)

fu3(66,177, irum='홍길동')
fu3(77,178, irum='고길동', nai=22)

print()
def fuFinal(a,b,*c,**d):
    print(a, ' ', b)
    print(c)
    print(d)
    
fuFinal(1, 2)
fuFinal(1, 2, 3, 4, 5)
fuFinal(1, 2, 3, 4, 5, m=6, n=7)


