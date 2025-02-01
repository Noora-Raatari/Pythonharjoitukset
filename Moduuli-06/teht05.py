def parittomat (tekijät):
    muokattu_lista = [i for i in tekijät if i %2 ==0]
    return muokattu_lista

def main ():
    lista = [3,7,2,8,9,11,13,4, 10,12,33]
    uusilista = parittomat(lista)
    print(f"Lista lukuja oli {lista}")
    print(f"Ja lista parittomat luvut poistettuna on{uusilista}  ")

main()