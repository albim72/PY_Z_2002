import time
from pizza import Pizza

class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5
        
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzDough.thin)
        
    def add_sauce(self):
        print('dodawanie sosu pomidorowego na powirzchnię ciasta...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('sos został nałożony')
        
    def add_topping(self):
        topping_desc = 'double_mozarella, oregano'
        topping_items = (PizzaTopping.double_mozarella, PizzaTopping.oregano)
        print(f'dodawanie składników na powierzchnię ciasta ({topping_desc})')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'składniki do pizzy dodane ({topping_desc})')
        
    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'pieczenie pizzy jeszcze {self.baking_time} s')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('twoja pizza jest gotowa!')
