class bank:
    def __init__(self):
        self.__balance = 1000

    def deposit(self , amount):
        self.__balance += amount

    def show(self):
        print("Current BAlance : " , self.__balance)

b1 = bank()
b1.deposit(700)

b1.show()