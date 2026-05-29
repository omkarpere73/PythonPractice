class human:
    def eat(self):
        print("Eating")

class student(human):
    def study(self):
        print("Studying")

s1 = student()
s1.eat()
s1.study()

