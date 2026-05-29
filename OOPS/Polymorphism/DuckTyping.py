# "If it behaves like a duck,
# treat it like a duck." - Duck typing

class student:
    def intro(self):
        print("Im a Student")

class teacher:
    def intro(self):
        print("Im a Teacher")

def introduce(person):
    person.intro()

p1 = teacher()
p2 = student()

introduce(p1)
introduce(p2)