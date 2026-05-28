class atm:
    def __init__(self , pin ):
        self.__pin = pin
        self.__balance = 0

    def deposit(self , pin , amount):
        if pin == self.__pin:
            self.__balance += amount
            print("Deposit Succesfull . Current Balance : " , self.__balance)
        else:
            print("Incorrect Pin")

    def withdraw(self , pin , amount):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal Succesfull")
            else:
                print("Unsufficient Amount")
        else:
            print("Incorrect Pin")

    def show(self , pin):
        if pin == self.__pin:
            print("Current Balance is " , self.__balance)

a1 = atm(0000)
a1.show(0000)

a1.deposit(0000 , 10000)

a1.withdraw(0000 , 5000)
a1.show(0000)