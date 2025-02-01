def summaus (tekijät):
    tulos = 0
    for i in tekijät:
        tulos += i
    return tulos

def main ():
    lista = [3,7,5]
    summa = summaus(lista)
    print(f"Lukujen {lista} summa on {summa}"  )

main()