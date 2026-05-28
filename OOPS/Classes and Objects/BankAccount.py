class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount

    def withdraw(self , amount):
        self.balance -= amount

    def show(self):
        print("Account Holder Name : " , self.name)
        print("Balance : " , self.balance)

a1 = BankAccount("Omkar" , 2000)

a1.deposit(500)
a1.withdraw(200)

a1.show()