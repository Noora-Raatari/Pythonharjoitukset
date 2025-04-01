class Hissi:
    def __init__(self, alin, ylin):
        self.kerros=alin
        self.alin= alin
        self.ylin= ylin

    def siirry_kerrokseen(self,hissi, tavoite):
        if self.kerros < tavoite:
            hissi.kerros_ylös(tavoite)
            print(f"olet nyt kerroksessa {self.kerros}")
        if self.kerros > tavoite:
            hissi.kerros_alas(tavoite)
            print (f"olet nyt kerroksessa {self.kerros}")

    def kerros_ylös(self,tavoite):
        if self.kerros < self.ylin:
            while self.kerros < tavoite:
                self.kerros= self.kerros +1
                print(f"hissi kulkee :) menossa kerros {self.kerros}")
        else:
            print("Olet jo ylimmässä kerroksessa")
    def kerros_alas(self,n, tavoite):
        if self.kerros > self.alin:
            while self.kerros > self.alin:
                self.kerros=self.kerros-1
                print(f"hissi kulkee :) menossa kerros {self.kerros}")
        else:
            print(f"Hissi {n} on jo alimmassa kerroksessa")

class Talo:
    def __init__(self, hissien_määrä,alin, ylin):
        self.ylin=ylin
        self.alin=alin
        self.hissien_määrä=hissien_määrä
        self.hissit=[]
        for h in range (self.hissien_määrä):
            self.hissit.append(Hissi(self.alin,self.ylin))

    def ajele_hissillä(self,hissi,tavoite):
        self.hissi = hissi +1
        self.tavoite = tavoite
        print(f"Hissi numero {self.hissi} lähtee liikkeelle")
        self.hissit[hissi].siirry_kerrokseen(self.hissit[hissi],self.tavoite)

    def palohälytys(self):
        print("Tulipalo! Kaikki hissit ajavat pohjakerrokseen")
        for n in range ((len(self.hissit))):
            self.hissit[n].kerros_alas(n+1,self.alin)


top=int(input("Montako kerrosta talossasi on?"))
kpl= int(input("Montako hissiä talossa on?"))

talo=Talo(kpl,1,top)

nro=int(input("Millä hissillä haluat liikkua? (nro)"))-1
goal=int(input("Mihin kerrokseen haluat mennä?"))
talo.ajele_hissillä(nro,goal)
talo.palohälytys()