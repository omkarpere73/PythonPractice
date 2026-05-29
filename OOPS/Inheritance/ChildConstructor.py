class Human:
    def __init__(self):
        print("Human Constructor")

class Student(Human):
    def __init__(self):
        print("Student Constructor")

s1 = Student()