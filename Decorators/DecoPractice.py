import logging
logging.basicConfig(level=logging.INFO)

def decologging(func):
    def decorated(*args , **kwargs):
        logging.info(f"Calling {func.__name__}")
        result = func(*args , **kwargs)
        logging.info(f"Your function {func.__name__} returned {result}")
        return result
    return decorated

@decologging
def myfunc(a , b):
    return a + b , a - b

myfunc(10 , 5)
