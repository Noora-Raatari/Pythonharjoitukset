nimi = "myyrä"
print("moi " + nimi + ", mitä kuuluu?")
print (f"Moi {nimi}, kuinkans nyt menee?")

#käyttäjän syötteen lukeminen
#lukuA = muuttuja jonka arvoon luetaan käyttäjän input
#input lukee kaikki syötteet aina merkkijonnoina, ei lukuina
lukuA_str = input("Anna kokonaisluku: ")
#muutetaan input samalla heti kokonaisluvuksi
lukuB = int (input ("Aika hyvä, anna toinen: ") )
#muutetaan merkkijono kokonaisluvuksi nyt myöhemmin
lukuA = int (lukuA_str)

summa = lukuA + lukuB
print(f"lukujesi summa = {summa}")