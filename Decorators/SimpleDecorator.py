def decor(func):
    def inner():
        print("Before Function Call")
        func()
        print("After Function Call")
    return inner

@decor
def greet():
    print("Hello")

greet()