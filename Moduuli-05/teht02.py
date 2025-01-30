lukujono =[]

luku_str= (input("Anna kokonaisluku tai lopeta painamalla enter"))

while luku_str != "":
    luku = int (luku_str)
    lukujono.append (luku)
    luku_str =(input("Anna seuraava kokonaisluku tai lopeta painamalla enter"))


lukujono.sort(reverse=True)
print (f"Luettelemistasi luvuista viisi suurinta olivat {lukujono [0:5]}" )