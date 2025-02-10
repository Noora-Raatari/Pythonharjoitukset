lentokentät = {}
def valikko():
    print("Valitse \n 1. Tallenna uusi lentokenttä \n 2. Hae lentokenttää \n 3. Lopeta ohjelma")
    return

def tallenna_uusi(koodi,kenttä):
    if koodi in lentokentät:
        print("Lentokenttä on jo listassa")
    else:
        print("Lentokenttä tallennettu")
        lentokentät [koodi] = kenttä
    return
def hae_lentokenttää(l):
    if l in lentokentät:
        print (f"Lentokenttä koodilla {l} on {lentokentät[l]}")
    else:
        print ("Lentokenttää ei löytynyt :((")
    return

valikko()
valinta = int (input("Valinta:"))
while valinta != 3:
    if valinta ==1:
        icao = input("Anna lentokentän ICAO-koodi")
        nimi = input ("Anna lentokentän nimi")
        tallenna_uusi(icao, nimi)
        valikko()
        valinta = int(input("Valinta:"))
    if valinta ==2:
        haku = input("Anna haettavan lentokentän ICAO-koodi:")
        hae_lentokenttää(haku)
        valikko()
        valinta = int(input("Valinta:"))
print("Ohjelma on päättynyt, baikkuu!!")


