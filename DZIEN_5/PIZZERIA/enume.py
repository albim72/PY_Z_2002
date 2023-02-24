from enum import Enum
import time


PizzaProgress = Enum('PizzaProgress','queued preparation baking ready')
PizzaDough = Enum('PizzaDough','thin thick')
PizzaSauce = Enum('PizzaSouce','tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping','mozarella double_mozarella bacon ham '
                                   'mushrooms red_onion oregano')

STEP_DELAY = 3 #w sekundach
