# 에러의 종류
# syntax error: 문법 오류
# logic : 프로그램 실행 중에 발생하는 오류로 프로그램이 비정상적으로 종료되는 오류
# exception : 예외란 코드를 실행하는 중에 발생한는 오류. try ~ except 문 사용

def divide(a, b):
    return a / b

print('뭔가를 하다가...')
'''
c = divide(5, 2)
c = divide(5, 0) # ZeroDivisionError: division by zero
print(c)
'''
try:
    #c = divide(5, 2)
    c = divide(5, 0)
    print(c)
    
    aa = [1,2]
    print(aa[0])
    # print(aa[2])
    
    f = open(r'c:/work/abc.txt')

    print('계속')
except ZeroDivisionError:
    print('두 번째 숫자는 0을 주지 마시오 ')
except IndexError as e:
    print('참조 범위 오류: ', e)
except Exception as err:        # 제일 마지막에 exception err를 적용
    print('에러 발생 : ', err)
finally:
    print('에러 유무에 상관없이 반드시 수행됨')

print('프로그램 종료')