def star(func):
    def wrapper():
        print("*" * 10)
        func()
        print("*" * 10)
    return wrapper

def hash(func):
    def wrapper():
        print("#" * 10)
        func()
        print("#" * 10)
    return wrapper

@star
@hash
def myfunc():
    print("Python")

myfunc()

