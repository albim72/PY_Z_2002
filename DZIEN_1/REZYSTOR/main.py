from oldresistor import OldResistor

r0 = OldResistor(50e3)
print(f'przed zmianą: {r0.get_ohms()} omów')
r0.set_ohms(14e2)
print(f'po zmianie: {r0.get_ohms()} omów')
