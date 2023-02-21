from typing import List,Protocol

class Item(Protocol):
    quantity:float
    price:float

class Product:
    def __init__(self,name:str,quantity:float,price:float):
        self.name = name
        self.quantity = quantity
        self.price = price

def calculate_total(items: List[Item]) -> float:
    return sum([item.quantity*item.price for item in items])

total = calculate_total([
    Product('towar A1',11,167),
    Product('towar F5',3,1099),
    Product('towar S5',8,99.6)
])

print(total)

class Stock:
    def __init__(self,product_name,quantity,price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


stotal = calculate_total([
    Stock('Telwizor',2,1240),
    Stock('Tablet',4,888)
])

print(stotal)






