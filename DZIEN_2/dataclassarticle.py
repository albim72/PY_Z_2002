from dataclasses import dataclass

@dataclass
class Article:
    title:str
    author:str
    content:str
    def __repr__(self):
        return f"{self.author} {self.content}"

@dataclass(init=False)
class PythonArticle(Article):
    language:str
    author:str
    price:int = 30

    def __repr__(self):
        return f"{self.language},{self.author},{self.price} zł, {self.title}"

    def __init__(self,title,price):
        self.title = title
        self.price = price
        self.language = "Python 3"
        self.author = "Marcin Albiniak"
        self.content = "Opis wybranych aspektów użycia języka Python"

    def infoart(self):
        return f'publikacja {self.title}, autor: {self.author}, cena: {self.price} zł -> rabat: {0.1*self.price} zł'

art = PythonArticle("Algorytmy DL",99)
print(art)
print(art.infoart())

a = Article("DDD","Janek","ABC")
