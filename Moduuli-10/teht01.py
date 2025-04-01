class Hissi:
    def __init__(self, alin, ylin):
        self.kerros=alin
        self.alin= alin
        self.ylin= ylin
    def siirry_kerrokseen(self, tavoite):
        print(f"Lähdet liikkeelle hissillä. Hissi lähtee kerroksesta {self.kerros}")
        if self.kerros < tavoite:
            hissi.kerros_ylös(tavoite)
            print(f"olet nyt kerroksessa {self.kerros}")
        if self.kerros > tavoite:
            hissi.kerros_alas(tavoite)
            print (f"olet nyt kerroksessa {self.kerros}")
    def kerros_ylös(self, tavoite):
        if self.kerros < self.ylin:
            while self.kerros < tavoite:
                self.kerros = self.kerros + 1
                print(f"hissi kulkee :) menossa kerros {self.kerros}")
        else:
            print("Olet jo ylimmässä kerroksessa")
    def kerros_alas(self, tavoite):
        if self.kerros > self.alin:
            while self.kerros > tavoite:
                self.kerros = self.kerros -1
                print(f"hissi kulkee :) menossa kerros {self.kerros}")
        else:
            print("Olet jo alimmassa kerroksessa")

hissi=Hissi(1,8)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)