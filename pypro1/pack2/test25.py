# 커피는 200원
class CoinIn:

    coin = 0
    change = 0

    def culc(self, cupCount):
        self.change = cupCount * 200
        return self.change

class Machine:
    def __init__(self):
        self.coin = CoinIn()

    cupCount = 1

    def showData(self):

        coin = int(input("동전을 입력하세요 : "))
        self.cupCount = int(input("몇 잔을 원하세요 : "))
        result = coin - self.coin.culc(self.cupCount)
        if result < 0:
            print("요금 부족")
        else:
            print("커피 {}잔과 잔돈 {}원".format(self.cupCount, result))


if __name__ == '__main__':
    Machine().showData()