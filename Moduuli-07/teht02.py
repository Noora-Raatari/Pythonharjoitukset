nimet = set ()
n= input("Anna nimi")
while n !="":
    nimet.add (n)
    n = input("Anna nimi")
    if n in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
else:
    print("Tässä kaikki annetut nimet:")
    for i in nimet:
        print (i)

