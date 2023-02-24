import time
from enume import *

class Pizza:
    def __init__(self,name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self,dough):
        self.dough = dough
        print(f'przygotowanie {self.dough.name} -> ciasto na {self}')
        time.sleep(STEP_DELAY)
        print(f'wykonanane na {self.dough.name} ciasto')
