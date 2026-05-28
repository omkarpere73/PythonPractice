class bank:
    def __init__(self):
        self.__balance = 1000

    def withdraw(self , amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(amount , "Withdraw Successfull")
        else:
            print("Unsufficient Balance")

    def show(self):
        print("Balance : " , self.__balance)

b1 = bank()
b1.show()

b1.withdraw(300)
b1.show()

b1.withdraw(500)
b1.show()

b1.withdraw(300)
b1.show()