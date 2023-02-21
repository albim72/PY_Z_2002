from dataclasses import dataclass
from datetime import datetime

@dataclass
class Person:
    firstname:str
    lastname:str
    year_of_birth:int

    @property
    def age(self):
        return datetime.now().year - self.year_of_birth

p = Person('Janusz','Gierej',1965)
print(p)
print(p.age)
