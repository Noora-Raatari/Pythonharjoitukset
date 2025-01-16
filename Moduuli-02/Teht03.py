import math

kanta_str= input("Anna suorakulmion kanta")
korkeus_str = input("Anna suorakulmion korkeus")

kanta = float (kanta_str)
korkeus= float (korkeus_str)

piiri = korkeus*2 + kanta*2
ala = korkeus*kanta
print (f" Suorakulmion piiri on {piiri:.2f} ja pinta-ala {ala:.2f}")