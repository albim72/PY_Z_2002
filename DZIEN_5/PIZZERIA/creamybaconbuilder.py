import time
from pizza import Pizza
from enume import *

class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('dodawanie sosu kremowego pomidorowego na powierzchnię ciasta...')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('sos został nałożony')

    def add_topping(self):
        topping_desc = 'mozarella, boczek, szynka, grzyby, czerwona_cebula, oregano'
        topping_items = (PizzaTopping.mozarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregano)
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
