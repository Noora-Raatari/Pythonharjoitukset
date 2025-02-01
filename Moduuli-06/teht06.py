import math

def pitsojen_hinta (halkaisija, hinta):
    pinta_ala = math.pi * (halkaisija/2)**2
    yksikkö_hinta = hinta/pinta_ala
    return yksikkö_hinta

def hintavertailu(p1,p2):
    if p1<p2:
        print ("Trust me bro, eka pitsa on enemmän vastinetta rahalle")
    else:
        print ("Trust me bro, toinen pitsa on enemmän vastinetta rahalle")
    return

def main ():
    p1_halkaisija = float (input("Anna ensimmäisen pitsasi halkaisija(cm)"))
    p1_hinta = float (input("Anna ensimmäisen pitsasi hinta(€)"))
    p2_halkaisija = float (input("Anna toisen pitsasi halkaisija (cm)"))
    p2_hinta = float (input("Anna toisen pitsasi hinta (€)"))
    pizza1 = pitsojen_hinta(p1_halkaisija, p1_hinta)
    pizza2 = pitsojen_hinta(p2_halkaisija, p2_hinta)
    hintavertailu(pizza1,pizza2)

main ()