import random
from tabulate import tabulate

class Auto:
    def __init__(self, nimi, rekisteri, huippunopeus):
        self.nimi = nimi
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = random.randint(50, huippunopeus)
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, matka_aika):
        self.matka += matka_aika * self.nopeus

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus, autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus = pituus
        self.autot = autot
        self.tunti = 0

    def tunti_kuluu(self):
        for auto in self.autot:
            kiihdytys = random.randint(-10, 15)
            auto.kiihdytä(kiihdytys)
            auto.kulje(1)


    def kilpailu_ohi(self):
        kilpailu_ohi=False

        while kilpailu_ohi == False:
            self.tunti =self.tunti + 1
            self.tunti_kuluu()
            tavoitematka = 0
            for auto in self.autot:
                if auto.matka > tavoitematka:
                    tavoitematka = auto.matka
            if tavoitematka >= self.pituus:
                kilpailu_ohi = True

            if self.tunti % 10 == 0:
                self.tilanne()
        return True

    def tilanne(self):
        self.autot.sort(key=lambda auto: auto.matka, reverse=True)
        print(f"\nKilpailun väliaikatiedot (Meneillään tunti {self.tunti})\n")
        for i in range(len(self.autot)):
            table = [
                ["Auton nimi", autot[i].nimi],
                ["Rekisterinumero", autot[i].rekisteri],
                ["Kuljettu matka", f"{autot[i].matka:.2f} km"],
                ["Nopeus", f"{autot[i].nopeus} km/h"]
            ]
            print(tabulate(table, tablefmt='fancygrid'))



autot = []
for i in range(1, 11):
    kilpa_auto = f"kilpa-auto {i}"
    autot.append(Auto(kilpa_auto, f"ABC-{i}", random.randint(150, 200)))


kilpailu = Kilpailu("Suuri romuralli", 10000, autot)

print(f"\n {kilpailu.kilpailun_nimi} alkaa")
kilpailu_ohi = False


kilpailu.kilpailu_ohi()


autot.sort(key=lambda auto: auto.matka, reverse=True)

print("\nKilpailu on päättynyt, tässä kaikkien 10 auton tulokset:\n")
for i in range(len(autot)):
    table = [
        ["Auton nimi", autot[i].nimi],
        ["Rekisterinumero", autot[i].rekisteri],
        ["Kuljettu matka", f"{autot[i].matka:.2f} km"],
        ["Nopeus", f"{autot[i].nopeus} km/h"]
    ]
    print(tabulate(table, tablefmt='fancygrid'))