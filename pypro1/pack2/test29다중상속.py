# 다중 상속
class Tiger: 
    data = "호랑이 세상"
    
    def cry(self):
        print('호랑이가 소리를 ...')
        
    def eat(self):
        print('맹수는 고기를 무척 좋아함')
        
class Lion:
    def cry(self):
        print('사자의 울부짖음')
        
    def hobby(self):
        print('백수의 왕은 채팅을 즐김')

class Liger1(Tiger, Lion):      # 다중 상속
    pass
    
obj1 = Liger1()
obj1.cry()                      # 중복 시 먼저 적은 멤버가 수행된다.
obj1.eat()     
obj1.hobby()
print(obj1.data)
    
print('----------------')
def hobby():
    print('모듈의 멤버인 함수')
    
class Liger2(Lion,Tiger):
    data = '라이거 만세'
    
    def play(self):
        print('라이거 고유 메소드')
        
    def hobby(self):
        print('Liger likes workout')
        
    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data + ", " + super().data)
        
obj2 = Liger2()        
obj2.cry()      
obj2.showHobby()  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        