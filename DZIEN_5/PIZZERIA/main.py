from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress','w kolejce do wypieku....')
PizzaDough = Enum('PizzaDough','cienkie ciasto')
PizzaSauce = Enum('PizzaSouce','kremowy sos pomidorowy')
PizzaTopping = Enum('PizzaTopping','mozarella double_mozarella boczek szynka '
                                   'grzyby czerwona_cebula oregano')

STEP_DELAY = 3 #w sekundach

