from abc import ABC  , abstractmethod

class vehicle(ABC):
    @abstractmethod
    def fueltype(self):
        pass

class car(vehicle):
    def fueltype(self):
        print("Diesel")

class bike(vehicle):
    def fueltype(self):
        print("Petrol")

v1 = car()
v1.fueltype()

v2 = bike()
v2.fueltype()