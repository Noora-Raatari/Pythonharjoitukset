import math

lukuA_str= input("Anna kokonaisluku")
lukuC_str =input ("Anna vielä yksi kokonaisluku")
lukuB_str = input("hyvä, mutta annapa toinen")

lukuA = int (lukuA_str)
lukuB= int (lukuB_str)
lukuC = int (lukuC_str)

summa = lukuA + lukuB + lukuC
tulo = lukuA * lukuB * lukuC
keskiarvo= (lukuA + lukuB + lukuC)/3

print (f" Lukujen summa on {summa} , tulo {tulo} ja keskiarvo {keskiarvo:.3f}")