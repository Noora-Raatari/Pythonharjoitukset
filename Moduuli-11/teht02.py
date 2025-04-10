import random


class Auto:
    def __init__(self, rekisteri, huippunopeus):
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

    def tunti_kuluu(self):
        for auto in autot:
            kiihdytys = random.randint(-10, 15)
            auto.kiihdytä(kiihdytys)
            auto.kulje(1)
    def tulosta_tiedot(self):
        print(f"\nAuton rekisterinumero: {self.rekisteri}")
        print(f"Auton kulkema matka: {self.matka}")

class Sähköauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akku):
        super().__init__(rekisteri, huippunopeus)
        self.akku = akku
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Auton tyyppi: sähköauto")

class Polttomoottori(Auto):
    def __init__(self, rekisteri, huippunopeus, tankki):
        super().__init__(rekisteri, huippunopeus)
        self.tankki = tankki
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Auton tyyppi: polttomoottoriauto")


autot = [Sähköauto("abc-15", 180, "52.5 kWh"), Polttomoottori("acd-123", 165, "32.2 l")]

for auto in autot:
    auto.kulje(3)

for auto in autot:
    auto.tulosta_tiedot()