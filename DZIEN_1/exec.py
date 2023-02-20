mycode = '''
a = 5
b = 56
print(f'a x b = {a*b}')
'''

exec(mycode)

import os
code = input('Co chcesz zrobić dzisiaj?')
exec(code)

def calulatePerimeter(l):
    return 4*l

def calculateArea(l):
    return l**2

expression = input("podaj typ funkcji: ")

for l in range(1,5):
    if(expression == 'calculatePerimeter(l)'):
        print(f"jeśli bok działki wynosi: {l}, obwód = {eval(expression)}")
    elif (expression == 'calculateArea(l)'):
        print(f"jeśli bok działki wynosi: {l}, pole powierzchni = {eval(expression)}")
    else:
        print("Zła funkcja")
        break
