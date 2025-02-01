import random

def nopanheitto(sivut):
    return random.randint(1,sivut)

def main ():
    n=0
    x= int (input("Montako sivua nopassasi on?"))
    noppa= nopanheitto(x)

    if noppa == x:
        n=n+1
        print(f"Heitto {n} : {noppa} ")
    while noppa !=x:
        noppa = nopanheitto(x)
        n = n +1
        print(f"Heitto {n} : {noppa} ")


main ()