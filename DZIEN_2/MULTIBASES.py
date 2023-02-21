class MultiBases(type):
    def __new__(cls, clasname,bases,attrs):
        if len(bases) > 1:
            raise TypeError('możliwe jest tylko jednodziedziczenie!')
        return super().__new__(cls, clasname,bases,attrs)


class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class Spec:
    pass

class B(Spec,A):
    pass
