class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"\nJulkaisun nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi,kirjailija, sivut):
        self.kirjailija = kirjailija
        self.sivut= sivut
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan sivumäärä: {self.sivut}")
        print(f"Kirjailijan nimi: {self.kirjailija}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Lehden päätoimittaja: {self.päätoimittaja}")



julkaisut = []

julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom","200"))

for julkaisu in julkaisut:
    julkaisu.tulosta_tiedot()
