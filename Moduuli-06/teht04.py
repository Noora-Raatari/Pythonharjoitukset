def summaus (tekijät: object) -> object:
    tulos = 0
    for i in tekijät:
        tulos += i
    return tulos

def main ():
    lista = [3,7,2]
    summa = summaus(lista)
    print(f"Lukujen {lista} summa on {summa}"  )

main()