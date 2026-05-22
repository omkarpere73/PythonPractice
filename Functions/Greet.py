def display(func):
    res = func()
    print("Hello "+res)

def func():
    return "Omkar"

display(func)