import time
from functools import wraps
def dec(func):
    @wraps(func)
    def d():
        print("this is test")
        s = time.time()
        func()
        e = time.time()
    return d

@dec
def dec2(func):
    @wraps(func)
    def d():
        print("this is test dec 2")
        s = time.time()
        func()
        e = time.time()
    return d

@dec2
def dec3(func):
    @wraps(func)
    def d():
        print("this is test dec 2")
        s = time.time()
        func()
        e = time.time()
    return d

@dec3
def test():
    print("test")

test()