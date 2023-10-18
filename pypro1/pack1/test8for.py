# 반복문 for
# for target in object: ...
from intake.cli.client.subcommands import list

for i in [1, 2, 3, 4, 5]:
    print(i, end=' ')
    
print()
for i in {1, 2, 3, 4, 5}:
    print(i, end=' ')

print()
for i in (1, 2, 3, 4, 5):
    print(i, end=' ')

print()
soft = {'java':'웹용언어', 'python':'만능언어', 'js':'웹용스크립트'}
for i in soft.items():
    # print(i)
    print(i[0] + '^^;' + i[1])
    
for k, v in soft.items():
    print(k)
    print(v)
    
print()
for aa in soft.keys():
    print(aa, end=' ')

print()
for bb in soft.values():
    print(bb, end=' ')

print()
# numbers = [1,3,5,7,9]
numbers = [-3, 4, 5, 7, 12]
tot = 0
for a in numbers:
    tot += a
    
print('합은 ' + str(tot) + ', 평균은 ' + str((tot / len(numbers))))

print()
li = ['a', 'b', 'c']
for k, d in enumerate(li):
    print(k, d)

print()
for n in [2, 3]:
    print('----{}단--'.format(n))
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('{}*{}={}'.format(n, i, n * i), end=' ')
    print()
    
print()
datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 2: continue
    if i == 4: break
    print(i, end=' ')
else:
    print('for 정상 종료')    
print()
jumsu = [95, 70 , 60, 55, 100]  # 70점 이상만 합격 처리
num = 0
for jum in jumsu:
    num += 1;
    if jum < 70:continue
    print('%d번째 합격' % num)
print('for + 정규표현식 연습--------')
import re
ss = """
정부는 10일 국무회의에서 고용노동부 소관 법령인 ‘국민 평생 직업능력 개발법’ 개정안을 심의·의결하고, 정기 국회에 제출할 예정이라고 밝혔습니다.정기 국회에 제출할 예정이라고 밝혔습니다.
이번 개정은 기업훈련 규제를 완화하는 특례제도를 도입하고, 고용노동부 장관의 권한 중 기능대학의 설립 추천권을 시·도지사에게 이양하여 기타 제도 운용상 나타난 일부 미비점을 개선·보완하게 됩니다.
"""
print(type(ss))
ss2 = re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
ss3 = ss2.split(' ')
print(ss3)

cou = {}  # 단어의 발생 횟수를 dict로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1 
    else:
        cou[i] = 1
print(cou)

print()
for ss in ['111-1234', '일이삼-이이이이', '234-6778']:
    if re.match(r'^\d{3,4}-\d{4}$', ss):
        print(ss, '전화번호 맞아요')
    else:
        print(ss, '전화번호 아닌 듯 ')

# 리스트 컴프리헨션은(List comprehension) 직관적으로 리스트를 생성하는 방법입니다. 대괄호"[","]"로 감싸고 내부에 for문과 if문을 사용하여 반복하며 조건에 만족하는 것만 리스트로 생성할 수 있습니다.
a = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)
print(list(i for i in a if i % 2 == 0))

print()
i1 = [3, 4, 5]
i2 = [0.5, 1, 2]
result = []
for a in i1:
    for b in i2:
        result.append(a + b)
print(result)
print('------')
datas = [a + b for a in i1 for b in i2]
print(datas)

print('List Comprehension 살펴보기 ---------')
temp = [1, 2, 3]
for i in temp:
    print(i, end=' ')
print()
print([i for i in temp])
print({i for i in temp})

print()
datas = [1, 2, 'a', True, 3]
li = [i * i for i in datas if type(i) == int]
print(li)

datas = {1, 1, 2, 2, 3, 2, 1}
imsi = {i * i for i in datas}
print(imsi)

print()
id_name = {1:'tom', 2:'oscar'}
print(id_name)
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
aa = [(1, 2), (3, 4), (5, 6)]
for a, b in aa:
    print(a + b)
    
# sum([1,2,3])
print('과일 값 계산 ---')
price = {'사과': 5000, '감':500, '배':1000}  # 오늘 과일 가격
guest = {'사과':3, '감':2}
bill = sum(price[f] * guest[f] for f in guest)
print('고객이 구매한 과일 총액은 {}원'.format(bill))

print('---range 함수---')
print(list(range(1, 11, 2)))
print(list(range(-10, -100, -20)))
print(set(range(1, 11, 2)))
print(tuple(range(1, 11, 2)))

print()
for i in range(6):  # 0이상 6미만 증가치 1
    print(i, end=' ')
    
print()
tot = 0
for su in range(1, 11):
    tot += su
print('결과: ' + str(tot))
print('내장함수 : ' + str(sum(range(1, 11))))

for _ in range(6):
    print('들자')
for i in range(1, 10):
    print('{0}*{1}={2}'.format(2, i, 2 * i))
    
# 문1 : 2 ~ 5단 출력
for n in [2, 3, 4, 5]:
    print('----{}단--'.format(n))
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('{}*{}={}'.format(n, i, n * i), end=' ')
    print()

print()    
# 문2 : 1 ~ 100 사이의 정수 중 3의 배수이면서 5의 배수의 합 출력
total = 0  # 합을 저장할 변수 초기화
for number in range(1, 101):  # 1부터 100까지의 정수를 반복
    if number % 3 == 0 and number % 5 == 0:  # 3의 배수이면서 5의 배수인 경우
        total += number  # 합에 해당 숫자를 더함

print("문제2 합은: ", total)

#반복문 for를 사용 : 1 ~ 100 사이의 숫자 중 3의 배수 또는 4의 배수 이고 7의 배수가 아닌 수를 출력하고
#건수와 합도 출력하는 코드를 작성하시오.
count = 0
total = 0

for number in range(1, 101):
    if (number % 3 == 0 or number % 4 == 0) and number % 7 != 0:
        print(number, end=' ')
        count += 1
        total += number

print("\n건수:", count)
print("배수의 총합:", total)

print()
# 문3 : 주사위를 두 번 던져 나오는 숫자들의 합이 4의 배수가 되는 경우만 출력
# 1 3 
# 2 6
# ...
for dice1 in range(1, 7):  # 첫 번째 주사위의 결과를 나타내는 루프
    for dice2 in range(1, 7):  # 두 번째 주사위의 결과를 나타내는 루프
        total = dice1 + dice2  # 주사위 두 번 던진 결과의 합 계산
        if total % 4 == 0:  # 합이 4의 배수인 경우만 출력
            print(f"첫 번째 주사위: {dice1}, 두 번째 주사위: {dice2}, 합: {total}")

for i in {1, 2, 3, 4, 5, 5, 5, 5}:
    print(i, end = ' ')

print()
print('---test----')
print(list(range(1, 6, 2)))






