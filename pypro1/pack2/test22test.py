class Bicycle:
    def __init__(self, name, wheel, price):
        self.name = name
        self.wheel = wheel
        self.price = price

    def calculate_price(self):
        return self.wheel * self.price

    def display(self):
        total_price = self.calculate_price()
        print(self.name + '님 자전거 바퀴 가격 총액은 ' + str(total_price) + '원 입니다.')

gildong = Bicycle('길동', 2, 50000)
gildong.display()


print('---문제13---')
while True:
    year = int(input("연도 입력: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(str(year) + "년은 윤년")
    else:
        print(str(year) + "년은 평년")
