from abc import ABC , abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("Bark")

class cat(animal):
    def sound(self):
        print("Meow")

a1 = dog()
a2 = cat()

a1.sound()
a2.sound()