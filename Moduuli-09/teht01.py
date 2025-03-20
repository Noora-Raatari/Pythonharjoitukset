class Auto:
    def __init__(self,rekisteri, huippunopeus, nopeus=0, matka=0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

auto= Auto("ABC-123", "142 km/h")

print (f"Auton \n rekisterinumero: {auto.rekisteri} \n huippunopeus:{auto.huippunopeus}\n "
       f"tämänhetkinen nopeus: {auto.nopeus} \n kuljettu matka:{auto.matka}")


