class CoffeeMachine:
    
    def __init__(self, coffee_count=10):
        self.coffee_price = 200  # 커피 가격
        self.balance = 0  # 투입된 
        self.coffee_count = coffee_count
    
    def insert_money(self):
        """금액을 투입하는 메서드"""
        amount = int(input("금액을 입력하세요: "))  # 사용자에게 금액 입력 요청
        if amount > 0:
            self.balance += amount
            print(f"{amount}원을 투입했습니다. 현재 잔액: {self.balance}원")
        else:
            print("유효하지 않은 금액입니다. 다시 시도하세요.")

    
    def select_coffee(self, coffee_type):
        if self.balance >= self.coffee_price and self.coffee_count > 0:
            print(f"{coffee_type} 커피 제공합니다. 잔액: {self.balance - self.coffee_price}원")
            self.balance -= self.coffee_price
            self.coffee_count -= 1
        elif self.coffee_count <= 0:
            print("커피가 모두 소진되었습니다.")
        else:
            print("잔액이 부족합니다. 금액을 더 투입하세요.")
        
        self.display_remaining_coffee_count()  # 남은 커피 갯수 표시

    def return_change(self):
        if self.balance > 0:
            print(f"{self.balance}원을 반환합니다.")
            self.balance = 0
        else:
            print("반환할 금액이 없습니다.")

    def display_remaining_coffee_count(self):
        print(f"남은 커피 갯수: {self.coffee_count}개")
  
# 모듈 테스트 코드
if __name__ == "__main__":
    coffee_machine = CoffeeMachine(10)  # 초기 커피 갯수 설정

    while coffee_machine.coffee_count > 0:
        coffee_machine.insert_money()
        coffee_machine.select_coffee("아메리카노")
        coffee_machine.return_change()
