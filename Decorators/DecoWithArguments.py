def deco(func):
    def inner(*args, **kwargs):
        print("Function is running")
        result = func(*args, **kwargs)
        return result

    return inner

@deco
def add(a, b):
    return a + b


print(add(10, 20))



