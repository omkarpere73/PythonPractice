class mobile:
    def __init__(self):
        self.__password = 0

    def setpassword(self , pin):
        self.__password = pin
        print("Password Set")

    def unlock(self , pin):
        if pin == self.__password:
            print("Unlocked")
        else:
            print("incorrect Pin")

m1 = mobile()
m1.setpassword(9090)

m1.unlock(0000)

