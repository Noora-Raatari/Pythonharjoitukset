import math
pienin= math.inf
suurin= -math.inf

luku_str= input("Anna luku")

while luku_str!="":
    luku= float (luku_str)
    if luku > suurin:
            suurin=luku
    if pienin>luku:
            pienin = luku
    luku_str = input("Anna luku")

print((f"suurin antamasi luku oli {suurin} ja pienin antamasi luku oli {pienin}"))