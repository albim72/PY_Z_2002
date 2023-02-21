from dataclasses import dataclass,astuple,asdict,field

@dataclass(order=True)
class Person:
    firstname:str = "Jan"
    lastname:str = "Nowak"
    age:int = 30
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)
    sort_index:int = field(init=False,repr=False)

    def __repr__(self):
        return f"Pracownik: {self.firstname} {self.lastname}, stanowisko: {self.job} -> fullname: {self.full_name}"

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname
        self.sort_index = self.age

janek =Person()
print(janek)

olga = Person("Olga","Kot",21,"sekretarka")
olga2 = Person("Henryk","Kot",23,"sekretarka")
print(olga)

janek_2 = Person(age=33)

print(janek_2<janek)
print(olga2>olga)

print(astuple(olga))
print(asdict(janek))


