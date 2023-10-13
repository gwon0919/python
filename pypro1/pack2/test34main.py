from pack2.test34etc import Employee

class Temporary(Employee):
    def __init__(self, irum, nai, ilsu, ildang):
        super().__init__(irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
    
    def pay(self):
        return self.ilsu * self.ildang
        
    def data_print(self):
        self.irumnai_print()
        print( ', 월급:{}'.format(self.pay()))

# t = Temporary('홍길동', 27, 20, 15000)
# t.data_print()

class Regular(Employee):
    def __init__(self,irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = salary
        
    def pay(self):
        return self.salary
        
    def data_print(self):
        self.irumnai_print()
        print(', 급여:{}'.format(self.pay()))
        
# r = Regular('한국인',27,3500000)
# r.data_print()

class Salesman(Regular):
    def __init__(self,irum,nai,salary,sales,commission):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commission = commission
        
    def pay(self):
        return int(self.salary + (self.sales*self.commission))
    
    def data_print(self):
        self.irumnai_print()
        print(', 수령액:{}'.format(self.pay()))
    
# s = Salesman('손오공',29,1200000,5000000,0.25)
# s.data_print()


t = Temporary('홍길동', 27, 20, 15000)
r = Regular('한국인',27,3500000)
s = Salesman('손오공',29,1200000,5000000,0.25)
t.data_print()
r.data_print()
s.data_print()










