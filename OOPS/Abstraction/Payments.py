from abc import ABC , abstractmethod

class payments(ABC):
    @abstractmethod
    def pay(self):
        pass

class upi(payments):
    def pay(self):
        print("Paying through upi")

class card(payments):
    def pay(self):
        print("Paying through card")

p1 = upi()
p1.pay()

p2 = card()
p2.pay()