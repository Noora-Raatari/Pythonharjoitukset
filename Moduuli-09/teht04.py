
import random
from tabulate import tabulate
kilpailu=True
class Auto:
    def __init__(self, nimi, rekisteri, huippunopeus ):
        self.nimi = nimi
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0




    def kiihdytä (self, nopeuden_muutos):
        self.nopeus= nopeuden_muutos + self.nopeus
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus <0:
            self.nopeus = 0

    def kulje (self,matka_aika):
        self.matka = self.matka + matka_aika * self.nopeus
tavoitematka = 0
autot =[]
kilpa_auto = 1
for i in range(1,11):
    kilpa_auto = f"kilpa-auto {i}"
    autot.append(kilpa_auto)


for i in range (len(autot)):
    autot[i]= Auto(autot[i], f"ABC-{i+1}", random.randint(100, 200))

kilpailu_käynnissä = True

while tavoitematka < 10000:
    for i in range (len(autot)):
        autot[i].kiihdytä(random.randint(-10,15))
        autot[i].kulje(1)
        if autot[i].matka > tavoitematka:
            tavoitematka = autot[i].matka
else:
    autot.sort(key=lambda n: n.matka, reverse=True)
    print("\nKilpailu on päättynyt, tässä kaikkien 10 auton tulokset: \n")
    for i in range (len(autot)):
       table = [["auton nimi",autot[i].nimi],["rekisterinumero", autot[i].rekisteri],["kuljettu matka",autot[i].matka]]
       print(tabulate(table, tablefmt='fancygrid'))







