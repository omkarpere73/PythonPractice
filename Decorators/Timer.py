import time
import logging
logging.basicConfig(level=logging.INFO)

def timer(func):
    def wrapper(*args ,**kwargs):
        start = time.time()
        logging.info(f"timer started")
        result = func(*args , **kwargs)
        end = time.time()
        logging.info(f"timer stopped")
        execution_time = end - start
        print(f"Execution time: {execution_time:.4f} seconds")
        return result
    return wrapper

@timer
def myfunc():
    for i in range(100000000):
        pass

myfunc()
