import xml.parsers.expat

source = """<?xml version='1.0' encoding='utf-8'?>
<parent id='top'>
    <child1 name='Ludvik'>Tak wabi się mój pies</child1>
    <child2 name='Buldog Angielski'>To jest jego rasa...</child2>
</parent>
"""


def start_element(name,attrs):
    print(f'start element: {name}, {attrs}')

def end_element(name):
    print(f'end element: {name}')

def char_data(data):
    print(f'dane: {repr(data)}')


p = xml.parsers.expat.ParserCreate()
p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

#p.Parse("<source c='67'>1234</source>")
#p.Parse("<source c='67'>1234</source>")

p.Parse(source)

