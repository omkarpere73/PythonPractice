class salary:
    def __init__(self):
        self.__salary = 0

    def set(self , sal):
        if sal > 0 :
            self.__salary = sal
        else :
            print("Invalid Salary")

    def get(self):
        print("Salary :" , self.__salary)

e1 = salary()
e1.set(10000)
e1.get()