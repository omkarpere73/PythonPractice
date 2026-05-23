import logging
logging.basicConfig(level=logging.INFO)

def loggingDeco(func):
    def decorated(*args , **kwargs):
        logging.info (f" Calling {func.__name__} with args = {args} and kwargs = {kwargs}")
        result = func(*args , **kwargs)
        logging.info (f" {func.__name__} returned {result}")
        return result
    return decorated

@loggingDeco
def myfunc(a, b):
    return a + b

myfunc(10 , 20)