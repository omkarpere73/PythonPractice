def uppercase(func):
    def wrapper(*args , **kwargs):
        result = func()
        return result.upper()
    return wrapper

@uppercase
def message():
    return msg

msg = str(input("Enter any String : "))

print(message())