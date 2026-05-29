class UPI:
    def pay(self):
        print("Payment using UPI")

class Card:
    def pay(self):
        print("Payment using Card")

def make_payment(method):
    method.pay()

u1 = UPI()
c1 = Card()

make_payment(u1)
make_payment(c1)