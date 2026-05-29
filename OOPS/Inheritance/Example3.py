class vehicle:
    def start(self):
        print("Vehicle started")

class car(vehicle):
    def __init__(self , brand):
        self.brand = brand

    def play(self):
        print(self.brand , "is playing music")

c1 = car("bmw")
c1.start()
c1.play()