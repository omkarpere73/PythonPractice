def votingcheck(func):
    def wrapper(*args , **kwargs):
        remaining = 18 - age
        if age >= 18:
            print(name , " you are eligible to vote")
        else:
            print(name , " you are not eligible to vote , you can vote in " , remaining , " years")
    return wrapper

@votingcheck
def myfunc(age , name):
    return age , name

name = str(input("Enter your name : "))
age = int(input("Enter your age : "))

myfunc(age)