class animal:
    def sound(self):
        print("Animal Sound")

class dog(animal):
    def sound(self):
        print("Bark")

d1 = dog()
d1.sound()