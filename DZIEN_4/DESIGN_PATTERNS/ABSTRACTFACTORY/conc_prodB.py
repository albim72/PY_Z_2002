from abstract_a import AbstractProductA
from abstract_b import AbstractProductB

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "wynik: produkt B1"

    def another_useful_method_b(self, collaborator: AbstractProductA) -> None:
        result = collaborator.useful_function_a()
        return f"wynik: B1 połączony z {result}"
    
class ConreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "wynik: produkt B2"

    def another_useful_method_b(self, collaborator: AbstractProductA) -> None:
        result = collaborator.useful_function_a()
        return f"wynik: B2 połączony z {result}"
