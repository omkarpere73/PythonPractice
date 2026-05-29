class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

d1 = Dog()
c1 = Cat()

make_sound(d1)
make_sound(c1)