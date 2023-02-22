import xml.sax

class UchwytFilmu(xml.sax.ContentHandler):

    def __init__(self):
        self.CurenntData = ""
        self.id = ""
        self.tytul = ""
        self.rok = ""
        self.kraj = ""
        self.czas_t = ""
        self.gatunek = ""

    def startElement(self,tag,attributes):
        self.CurenntData = tag
        if tag == "film":
            print("________________ FILM __________________")

    def endElement(self,tag):
        if self.CurenntData == "id_filmu":
            print(f"indentyfikator filmu: {self.id}")
        elif self.CurenntData == "tytul":
            print(f"tytuł filmu: {self.tytul}")
        elif self.CurenntData == "rok":
            print(f"rok produkcji filmu: {self.rok}")
        elif self.CurenntData == "kraj":
            print(f"kraj produkcji filmu: {self.kraj}")
        elif self.CurenntData == "czas_trwania ":
            print(f"czas twania filmu: {self.czas_t}")
        elif self.CurenntData == "gatunek":
            print(f"gatunek filmu: {self.gatunek}")

    def characters(self,content):
        if self.CurenntData == "id_filmu":
            self.id = content
        elif self.CurenntData == "tytul":
            self.tytul = content
        elif self.CurenntData == "rok":
            self.rok = content
        elif self.CurenntData == "kraj":
            self.kraj = content
        elif self.CurenntData == "czas_trwania":
            self.czas_t = content
        elif self.CurenntData == "gatunek":
            self.gatunek = content


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)

handler = UchwytFilmu()
parser.setContentHandler(handler)
parser.parse("filmy.xml")
