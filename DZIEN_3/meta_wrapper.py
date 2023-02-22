from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"pełna nazwa metody: {func.__qualname__}")
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls


class DebugMeta(type):
    def __new__(cls, clsname,bases,attrs):
        obj = super().__new__(cls, clsname,bases,attrs)
        obj = debugmethods(obj)
        return obj


class Base(metaclass=DebugMeta):pass
class Calc(Base):
    def add(self,x,y):
        return x+y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y

class SpecC(Base):
    def fx(self,a,b,c):
        return a**(b-c)

mc = Calc()

print(mc.add(3,6))
print(mc.mul(3,6))
print(mc.div(3,6))

sc = SpecC()
print(sc.fx(4,1,7))
