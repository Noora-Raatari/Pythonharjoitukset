def yksikkömuunnos(g):
        l= g*3.785
        return l
def main ():
    gallona = float (input("Anna gallonat, jotka muunnetaan litroiksi"))

    while gallona>0:
        tulos =yksikkömuunnos(gallona)
        print (f'Antamasi gallonat ovat muunnettuna {tulos:.2f} litraa')
        gallona = float (input("Anna gallonat, jotka muunnetaan litroiksi"))
    else:
        print ("Annoit negatiivisen luvun, ohjelma päättyi")


main()