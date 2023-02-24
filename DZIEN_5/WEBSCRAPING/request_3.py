import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r.url)
print(r.status_code)

soup = BeautifulSoup(r.content,'html.parser')
#print(soup.prettify())

print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)
print("_______________________________________________________")
s = soup.find('div',class_ = 'entry-content')
print(s)
print("_______________________________________________________")
g = soup.find('div',id = 'main')
print(g)
print("_______________________________________________________")
print("tekst z taga div...")
lines = s.find_all('p')
for line in lines:
    print(line.text)
