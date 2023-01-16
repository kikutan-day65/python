# decorator

# create performance decorator
# thanks to this decorator, we can check how long the function takes to execute
# it's useful, that's why we use decotrator
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1}s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i*5

long_time()