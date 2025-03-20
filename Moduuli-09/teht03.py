class Auto:
    def __init__(self,rekisteri, huippunopeus, nopeus=0, matka=0, ):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    def kiihdytä (self, nopeuden_muutos):
        self.nopeus= nopeuden_muutos + self.nopeus
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus <0:
            self.nopeus = 0
    def kulje (self,matka_aika):
        self.matka = matka_aika * self.nopeus


auto= Auto("ABC-123", 142)

print (f"Auton \n rekisterinumero: {auto.rekisteri} \n huippunopeus:{auto.huippunopeus} km/h\n "
       f"tämän hetkinen nopeus: {auto.nopeus} km/h \n kuljettu matka:{auto.matka}")
auto.kiihdytä(30)

print (f"\nAuton nopeus 1. kiihdytyksen jälkeen: {auto.nopeus}")

auto.kiihdytä(70)
print (f"Auton nopeus 2. kiihdytyksen jälkeen: {auto.nopeus}")

auto.kiihdytä(50)
print(f"Auton nopeus 3. kiihdytyksen jälkeen: {auto.nopeus}")

auto.kiihdytä(-60)
print (f"Auton nopeus hidastuksen jälkeen: {auto.nopeus} km/h")
ajoaika = 2
auto.kulje(ajoaika)
print(f"\nAuto on kulkenut nopeudella {auto.nopeus} km/h {ajoaika}h \nKuljettu matka on {auto.matka} km")


