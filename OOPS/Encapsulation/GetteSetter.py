class marks:
    def __init__(self):
        self.__marks = 0

    def set(self , marks):
        if marks >= 0 and marks < 100 :
            self.__marks = marks

        else :
            print("invalid marks")

    def get(self):
        print(self.__marks)

s1 = marks()
s1.set(100)
s1.get()
