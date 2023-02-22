import xml.etree.ElementTree as ET
try:
    tree = ET.parse("kraj.xml")
    root = tree.getroot()

    for child in root:
        print(f"tag: {child.tag}, atrybuty: {child.attrib}")

    print(root[0])
    print(root[0][2])
    print(root[0][2].text)
    print(root[2].text)

except:
    print("element  nie istnieje")

