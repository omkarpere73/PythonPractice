import logging
logging.basicConfig(level=logging.INFO)

def decologging(func):
    def decorated(*args , **kwargs):
        logging.info(f"Calling {func.__name__}")
        result = func(*args , **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@decologging
def myfunc(x , y):
    return x * y

myfunc(40 , 10)
