import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
r = http.request('GET','https://authoraditiagarwal.com')
