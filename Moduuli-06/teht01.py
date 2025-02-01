import random

def nopanheitto():
    return random.randint(1,6)

def main ():
    n=0
    noppa= nopanheitto()
    if noppa == 6:
        n = n + 1
        print(f"Heitto {n} : {noppa}")
    while noppa !=6:
        noppa = nopanheitto()
        n = n +1
        print(f"Heitto {n} : {noppa} ")



main ()