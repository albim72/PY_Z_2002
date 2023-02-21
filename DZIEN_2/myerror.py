class MyError(Exception):
    def __init__(self,x):
        self.x=x
    def __str__(self):
        print('wywołanie metody str')
        return f'wrtość x ={self.x} powienna wynosić 100'

try:
    x = int(input('podaj wartość x: '))
    if x != 100:
        raise MyError(x)
except MyError as m:
    print(m)
