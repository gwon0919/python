# Singleton pattern

class SingletonClass:
    inst = None
    
    def __new__(cls):   # 객체 생성을 담당. init에 의해 초기화됨
        if cls.inst is None:
            cls.inst = object.__new__(cls)
        return cls.inst

    def aa(self):
        print('난 메소드야')
        
class SubClass(SingletonClass):
    pass

s1 = SubClass()
s2 = SubClass()       
print(id(s1),id(s2))    # 2433056932624 2433056932624

s1.aa()
s2.aa()

print('----------------')
# 클래스의 멤버 변수를 고정
class Ani:
    __slots__ = ['irum', 'nai']
    
    def printData(self):
        print(self.irum, self.nai)
    
a = Ani()
a.irum = '호랑이'
a.nai = 3
# a.eat = '치킨' # 클래스의 멤버를 고정시켜 넣을 수 없다 (__slots__)
a.printData()    
        