from typing import Any


class MyInt(type):
    def __call__(cls, *args, **kwds):
        print("***** Here's My int *****", args)
        print("Now do watever you want with these objects...")
        return type.__call__(cls, *args, **kwds)
    
class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4,5)

print("****************####*****************")

class MetaSingleton(type):
    _instances = {}
    def __call__(self, *args, **kwds):
        if cls not in cls._instances:
            cls._instance[cls] = super(MetaSingleton, \cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
    
