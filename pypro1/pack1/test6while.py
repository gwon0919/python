# 반복문 while
a = 1

while a <= 5:
    print(a, end = ' ')
    a +=1
print()

i = 1
while i <= 3:
    j = 1
    while j <=4:
        print('i=' + str(i) + "\j=" + str(j))
        j = j + 1
    i += 1

print('1 ~ 100 사이의 정수 중 3의 배수의 합')
i = 1; hap = 0
while i <= 100:
    if i % 3 == 0:
        hap += i 
    i += 1
print('합은 ' + str(hap))

print()
colors = 'r', 'g', 'b'
print(colors[1])
a = 0
while a < len(colors):
    print(colors[a], end = ' : ')
    a+=1

print()
print('별 찍기')
i = 1
while i <= 10:
    j = 1
    disp = ''
    while j <= i:
        disp += '*'
        j += 1
    print(disp)  
    i += 1
    
print('\n문1 : 1 ~ 100 사이의 정수 중 3의 배수이거나 2의 배수가 아닌 수를 출력하고 그 합을 출력') 
i = 1; hap = 0
while i <= 100:
    if i % 3 == 0 and i /2 != 0:
        hap += i 
    i += 1
    print(str(hap))
        
print('\n문2 : 2 ~ 5 단의 구구단. 단이 다르면 다음 행으로 출력')

import time
#time.sleep(3)
#print('계속')

#===============================================================================
# button = input('폭탄 스위치를 누를까요?(y/n)')
# if button == 'Y' or button == 'y':
#     #pass
#     count = 5
#     while 1 <= count: 
#         print('%d초 남았군요'%count)
#         time.sleep(1)
#         count -= 1
#     print('BOOOM!')
# elif button == 'N' or button == 'n':
#     print('작업 취소')
# else:
#     print('y or n 을 누르시오')
#     
#===============================================================================
    
print('---test---')
print('별 찍기')
i = 1
while i <= 10:
    j = 1
    disp = ''
    while j <= i:
        disp += '*'
        j += 1
    print(disp)  
    i += 1
    
    
print()
num = 10
n = num
k = num + 1
while num > 0:
    print(" " * (k-num), "*" * num)
    num -=1

n = 10
k = n + 1
while n > 0:
    print(" " * (k-n), "*" * n)
    n -=1   
    

print('문제13')
number = 1
while number <= 100:
    if number % 10 == 3:
        print(number)
    number += 1
print()   
#===============================================================================
# i = 0
# while True:
#     if i<= 100:
#         i +=1
#          
#     if i >100 : False
#      
#     print(i, end=' ')
#      
i = 0
while True:
    if i <= 100:
        i += 1
        if i % 10 == 3:
            print(i, end=' ')
    if i > 100:
        break

