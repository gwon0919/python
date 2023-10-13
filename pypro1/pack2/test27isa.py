# 상속 연습
print('클래스는 모듈의 멤버')

class Person:
    say = '나 이런 사람이야~'      # public 
    nai = '20살'
    __my = 'private member'   # private '__'my
      
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
    
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai,self.say))
        
    def hello(self):
        print('안녕')
        print(self.__my)
        
    @staticmethod
    def kbs(tel):
        print('kbs_static method(클래스 소속)', tel)
        
        
        
print(Person.say, Person.nai)
# Person.printInfo(self)
p = Person('25')
print(p.say, p.nai)
p.printInfo()

p.hello()
p.kbs('111-1111')
Person.kbs('222-3456')  # 권장

print('***'*20)
class Employee(Person):
    subject = '근로자'
    
    def __init__(self):
        print('Employee 생성자')
        
    def printInfo(self):    # method overriding
        print('Employee의 오버라이딩된 printInfo')
        
    def eprintInfo(self):
        print(self.say, super().say)    # super() 부모클래스에서 받아온다
        self.hello()
        self.printInfo()
        super().printInfo()             # super는 바로 상위클래스로 이동한다.+
        
e = Employee()
print(e.say, e.subject)
e.eprintInfo()

print('***'*20)
class Worker(Person):
    say = 'worker의 say'
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)       # Bound method call
    
    def printInfo(self):
        print('Worker의 선언된 printInfo')
    
    def wprintInfo(self):
        self.printInfo()
        super().printInfo()

w = Worker('30')
print(w.say, w.nai)
w.wprintInfo()

print("^^^" * 20)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        super().__init__(nai)       # Bound call
        Worker.__init__(self, nai)  # UnBound call
        
    def pprintInfo(self):
        self.wprintInfo()
        
    def hello2(self):
        print('하이루')
        # print(self.__my)     # err : private member이므로 
        
pr = Programmer('33')
print(pr.say,pr.nai)
pr.pprintInfo()

pr.hello2()
pr.kbs('123-5678')
Programmer.kbs('222-3456')

print('---클래스 타입 확인---')
print(type(1.2))    # <class 'float'>
print(type(pr))     # <class '__main__.Programmer'>
print(Programmer.__bases__)     # (<class '__main__.Worker'>,) -> 집합형으로 나오는 이유는 다중상속이 가능하기 때문이다.
print(Worker.__bases__)         # (<class 'object'>,)
print(Person.__bases__)         # (<class 'object'>,)

























        