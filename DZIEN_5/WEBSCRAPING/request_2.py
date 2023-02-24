import re
import urllib.request

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Airplane!')
html = response.read()
text = html.decode()
e = re.findall('<div class="vector-menu-heading">',text)
print(e)
