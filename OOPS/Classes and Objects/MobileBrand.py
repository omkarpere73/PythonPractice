class Mobile:
    def __init__(self , brand , price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Mobile Brand = " , self.brand)
        print("Mobile Price = " , self.price)

m1 = Mobile("Samsung" , 120000)
m2 = Mobile("Apple" , 150000)

m1.display()