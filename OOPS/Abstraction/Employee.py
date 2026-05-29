from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Writing Code")

class Designer(Employee):
    def work(self):
        print("Designing UI")

d1 = Developer()
d2 = Designer()

d1.work()
d2.work()