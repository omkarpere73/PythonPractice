class employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def bonus(self , bonus):
        self.salary += bonus

    def display(self):
        print("Name : " , self.name)
        print("Salary : " , self.salary)

e1 = employee("Omkar" , 90000)
e1.bonus(20000)

e1.display()


