class MojaMeta(type):
    def __new__(cls,clsname,bases,attrsdict):
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy: {bases}")
        print(f"zbiór atrybutów: {attrsdict}")
        return type.__new__(cls,clsname,bases,attrsdict)

class Regular:
    pass

r = Regular()

class Main(Regular,metaclass=MojaMeta):
    @property
    def wara(self):
        return "wartość a"

mm = Main()

class B(Main):
    pass

class Pusta:
    pass

class C(Pusta,B):
    pass

class Kompozyt:
    f = Main()

    def __new__(cls, *args, **kwargs):
        return C()
    def __init__(self,ob):
        self.ob = ob

k = Kompozyt(Main())
