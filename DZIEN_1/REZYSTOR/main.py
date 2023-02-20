from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance


r0 = OldResistor(50e3)
print(f"____________{r0.__class__.__name__}______________")
print(f'przed zmianą: {r0.get_ohms()} omów')
r0.set_ohms(14e2)
print(f'po zmianie: {r0.get_ohms()} omów')

r1 = Resistor(34e3)
print(f"____________{r1.__class__.__name__}______________")
r1.ohms = 10e3
print(f'oporność: {r1.ohms} omów,\n'
      f'napięcie prądu: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A\n')

r2 = VoltageResistance(1e2)
print(f"____________{r2.__class__.__name__}______________")
print(f'natężenie początkowe prądu: {r2.current:.2f} A')
print(f'napięcie początkowe prądu: {r2.voltage:.2f} V')
r2.voltage  = 70

print(f'natężenie prądu: {r2.current:.2f} A')
print(f'napięcie prądu: {r2.voltage:.2f} V')

r3 = BoundedResistance(1.2e3)
print(f"____________{r3.__class__.__name__}______________")
try:
      r3.ohms = 1200
except ValueError as ve:
      print(ve)
else:
      print(f'oporność: {r3.ohms} omów')

finally:
      print("koniec tworzenia obwodu...")
