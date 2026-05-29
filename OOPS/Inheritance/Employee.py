class employee:
    def login(self):
        print("Login Succesfull")

class developer(employee):
    def start(self):
        print("Started Developement")

class manager(employee):
    def start(selfself):
        print("Started Management")

d1 = developer()
m1 = manager()

d1.login()
d1.start()

m1.login()
m1.start()