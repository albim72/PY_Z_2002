import urllib3
from bs4 import BeautifulSoup
from lxml import html

http = urllib3.PoolManager()
r = http.request('GET','https://authoraditiagarwal.com')
soup = BeautifulSoup(r.data,'lxml')
print(soup.title)
print(soup.title.text)
