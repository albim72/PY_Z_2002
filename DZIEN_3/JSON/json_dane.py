import json

jsonperson = '{"name":"Jan","lastname":"Nowak","city":"Kraków","age":46}'

print(jsonperson)
print(type(jsonperson))
person = json.loads(jsonperson)
print(person)
print(type(person))
print(person["city"])

car = {
    "marka":"Jeep",
    "model":"Cherokee",
    "rok":2019,
    "pojemnosc":[4.2,3.8,2.2,6.4]
}
jsoncar = json.dumps(car,indent=4)
print(jsoncar)

with open("car.json","w",encoding="utf-8") as f:
    f.write(jsoncar)

with open("car.json","r",encoding="utf-8") as f:
    car_dict = json.load(f)


print(car_dict)

print(car_dict["pojemnosc"][-1])

info = '{"organizacja":"Fundacja BIOTECH","miasto":"Krosno","kraj":"Polska"}'
extra = {"id":63544,"zakres":"algorytmy AI"}

z = json.loads(info)
z.update(extra)

info_new = json.dumps(z)
with open("biotech.json","w",encoding="utf-8") as f:
    f.write(info_new)

