class ATM:
    def __init__(self , balance):
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount

    def withdraw(self , amount):
        self.balance -= amount

    def show(self):
        print("Current Balance : " , self.balance)

a1 = ATM(1000)

a1.deposit(100)
a1.withdraw(200)
a1.deposit(400)

a1.show()