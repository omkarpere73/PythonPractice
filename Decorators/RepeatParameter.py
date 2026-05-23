def repeat(times):
    def decorator(func):
        def wrapper(*args , **kwargs):
            for i in range(times):
                func()
        return wrapper
    return decorator

@repeat(10)
def myfunc():
    print("Hello Omkar")

myfunc()
