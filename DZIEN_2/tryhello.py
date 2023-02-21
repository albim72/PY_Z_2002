class HelloMeta(type):
    def hello(cls):
        print(f"informacja od {type(cls())}")

    def __call__(self, *args, **kwargs):
        cls = type.__call__(self,*args)
        setattr(cls,'hello',self.hello)
        return cls

class TryHello(object,metaclass=HelloMeta):
    def MyHello(self):
        self.hello()

hej = TryHello()
hej.MyHello()
