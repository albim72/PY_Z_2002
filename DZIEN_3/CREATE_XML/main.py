from xml.etree.ElementTree import Element,SubElement
import xml.etree.ElementTree as ET
from prettyfy import pretty


top = Element('autokomis')

#pierwszy samochód
sam = SubElement(top,'samochod')

id = SubElement(sam,'id')
id.text = 'sam1'

marka = SubElement(sam,'marka')
marka.text = 'Subaru'

model = SubElement(sam,'model')
model.text = 'Impreza'

poj = SubElement(sam,'pojemnosc')
poj.text = '2.0'

przebieg = SubElement(sam,'przebieg')
przebieg.text = '198790'

rok = SubElement(sam,'rocznik')
rok.text = '1999'

cena = SubElement(sam,'cena')
cena.text = '61900'

wyp_dod = SubElement(sam,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czarna perła'

klima = SubElement(wyp_dod,'klimatyzacja')
klima.text = 'FGR425435'

pod = SubElement(wyp_dod,'poduszki_dod')
pod.text = '4'

#drugi samochód
sam = SubElement(top,'samochod')

id = SubElement(sam,'id')
id.text = 'sam2'

marka = SubElement(sam,'marka')
marka.text = 'Subaru'

model = SubElement(sam,'model')
model.text = 'Outback'

poj = SubElement(sam,'pojemnosc')
poj.text = '3.2'

przebieg = SubElement(sam,'przebieg')
przebieg.text = '87599'

rok = SubElement(sam,'rocznik')
rok.text = '2019'

cena = SubElement(sam,'cena')
cena.text = '145600'

wyp_dod = SubElement(sam,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czarna perła'

klima = SubElement(wyp_dod,'klimatyzacja')
klima.text = 'FGR425435'

pod = SubElement(wyp_dod,'poduszki_dod')
pod.text = '4'
