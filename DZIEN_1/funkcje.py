print("kilka przykładów funkcji...")

print((lambda e:e**4)(43))

b = lambda u,z=13:(u+90)*z
print(b(4,8))
print(b(9))

def multi(n):
    return lambda a:a*n

print(multi(6)(3))

#przukład -> filtrowanie listy
num = [67,2,5,-56,4,0,16,101,-33,56,999,-23,0,4,12,2]
