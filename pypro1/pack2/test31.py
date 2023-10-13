# 다중 상속 연습
class Animal:
    def move(self):
        pass
    
class Dog(Animal):
    name = "구름이"
    def move(self):
        print('구름이는 두 달에 한 번씩 미용실에 감')
    
class Cat(Animal):
    name = "냐옹이"
    
    def move(self):
        print('냐옹이는 한 달에 한 번씩 pc방에 감')
        print('밤에 눈빛이 빛남')
        
class Wolf(Dog,Cat):
    pass

class Fox(Cat, Dog):
    def move(self):
        print('난 여우라고 해')
        
    def foxMethod(self):
        print('여우 고유 메소드')

dog = Dog()
print(dog.name)
dog.move()
print()
cat = Cat()
print(cat.name)
cat.move()

print('---------------')
wolf = Wolf()
print(wolf.name)
wolf.move()
print()
fox = Fox()
print(fox.name)
fox.move()
fox.foxMethod()
print(Wolf.__mro__)         # __mro__ 클래스의 탐색 순서를 알 수 있다.
print(Fox.__mro__)
Animal

print('---------------')
sbs = wolf
sbs.move()
print()
sbs = fox
sbs.move()

print('---------------')
animals = (dog, cat, wolf, fox)
for a in animals:
    a.move()
    print()
    















        
    