# 추상 

from abc import ABCMeta, abstractmethod

class Friend(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def hobby(self):
        pass
    
    def printName(self):
        print('이름은 ' + self.name)
        
# 일반 
class John(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr
        
    def hobby(self):
        print(self.addr + ' 거리를 산책함')
        
    def printAddr(self):
        print('주소는 ' + self.addr)

class Chris(Friend):
    def __init__(self, name, addr):
        super().__init__(name)
        self.addr = addr
        
    def hobby(self):
        print(self.addr + ' 동네를 어슬렁 거림')
        print(self.addr + '에 오래 전부터 살고 있다.')
        
john = John('mr. John','역삼 1동')
john.printName()
john.printAddr()
john.hobby() 
print()
chris = Chris('mr. chris','역삼 2동')
chris.printName()
chris.hobby() 
print('----------------') 
fri = john
fri.hobby() 
print()
fri = chris 
fri.hobby()     
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        
    