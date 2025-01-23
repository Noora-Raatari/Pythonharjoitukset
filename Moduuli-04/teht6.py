import math
import random

N= (float (input("Anna arvottavien pisteiden määrä")))
n=0 #pisteet ympyrän sisässä
toistot = 0 #toistetaan arvonta niin kauan että on tehty N määrä

while toistot<N:

    y= random.uniform (-1,1)
    x=random.uniform (-1, 1)
    if x**2 + y**2 < 1:
        n= n +1 #lisätään piste n määrään kun löydetään sellainen
    toistot = toistot + 1

tulos = (4*n)/N
print(f"Piin likiarvo on {tulos}")
