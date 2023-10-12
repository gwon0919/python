# Class 멤버 호출

kor = 100

def abc():
    print('모듈의 멤버 함수')

class MyClass:
    kor = 90
    
    def abc(self):
        print('abc method')
        
    def show(self):
        # kor = 80
        # print(self.kor)
        print(kor)      # 변수 호출 순서 : 지역변수 > 모듈변수  
        self.abc()      # 클래스의 멤버 메소드 호출
        abc()           # 모듈의 멤버인 함수를 호출

my = MyClass()
my.show()

from pack2.test20other import Our
print(Our.a)
print('our1 ------')
our1 = Our
print(our1.a)
our1.a = 2
print('our2 ------')
our2 = Our
print(our2.a)































