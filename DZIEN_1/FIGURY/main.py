from trojkat import Trojkat
from prostokat import Prostokat
from trapez import Trapez
from kolo import Kolo

tr = Trojkat(6.6,7.3)
print(f"pole figury: {tr.__class__.__name__} wynosi {tr.policz_pole():.2f} cm2")

pr1 = Prostokat(4.7,8.9)
print(f"pole figury: {pr1.__class__.__name__} wynosi {pr1.policz_pole():.2f} cm2")

pr2 = Prostokat(6.2,6.2)
print(f"pole figury: {pr2.__class__.__name__} wynosi {pr2.policz_pole():.2f} cm2")

trp = Trapez(8.8,6.4,5.1)
print(f"pole figury: {trp.__class__.__name__} wynosi {trp.policz_pole():.2f} cm2")

kl = Kolo(5.6)
print(f"pole figury: {kl.__class__.__name__} wynosi {kl.policz_pole():.2f} cm2")
