import types

def notify(fn,*args,**kwargs):
    def fncomposite(*args,**kwargs):
        print(f"uruchomiono {fn.__name__}")
        rt = fn(*args,**kwargs)
        return rt
    return fncomposite

class Notifies(type):

    def __new__(cls, name, bases, attrs):
        for name,value in attrs.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attrs[name] = notify(value)
        return super(Notifies,cls).__new__(cls, name, bases, attrs)


class Maths(metaclass=Notifies):
    def multiply(a,b):
        prod = a*b
        print(prod)
        return prod

Maths.multiply(6,7)

class Fight(metaclass=Notifies):
    def battle(self):
        print("wyprowadź uderzenie...")

    def printu(self):
        u = "karabin"
        print(u)

    class Spec:
        pass
    sp = Spec()

s = Fight()
s.battle()
s.printu()
s.sp


