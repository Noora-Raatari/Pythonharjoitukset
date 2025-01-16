gramma = 1
luoti = 13.1 * gramma
naula = luoti  * 32
leiviska =  naula * 20

lukuA_str = input("Anna leiviskät")
lukuB_str = input ("Anna naulat")
lukuC_str = input("Anna luodit")

lukuA= float (lukuA_str)
lukuB = float (lukuB_str)
lukuC = float (lukuC_str)

paino_g = (luoti * lukuC) + (naula * lukuB) + (leiviska * lukuA)
paino_kg = paino_g / 1000
grammat = paino_g%1000
print (f"paino nykymitoissa {paino_kg} kg ja {grammat:.2f} g")

