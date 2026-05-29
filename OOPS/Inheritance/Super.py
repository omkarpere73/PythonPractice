class human:
    def __init__(self):
        print("Parent Constructor")

class student(human):
    def __init__(self):
        super().__init__()
        print("Student Constructor")

s1 = student()