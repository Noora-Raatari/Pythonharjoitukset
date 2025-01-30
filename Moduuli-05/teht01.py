import random

nopat=int (input("Montako noppaa heität?"))
tulos=0
for n in range(0,nopat):
    luku=random.randint(1,6)
    print (f"Heitto {n+1} : {luku}")
    tulos +=luku

print (tulos)

