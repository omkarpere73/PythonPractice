def handle_error(func):
    def wrapper(*args, **kwargs):
        try :
            return func(*args, **kwargs)
        except Exception as e :
            print("Error : " , e)

    return wrapper

@handle_error
def myfunc(x, y):
    print( "Result : " , x / y )
x = int(input("Enter divident : "))
y = int(input("Enter divisor : "))

myfunc(x , y)