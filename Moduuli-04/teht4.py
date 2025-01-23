import random

valittu_luku=random.randint(1,10)
luku=int(input("Arvaa luku"))
while luku!=valittu_luku:
    if luku<valittu_luku:
        print("Liian pieni")
        luku = int(input("Arvaa luku"))
    if luku>valittu_luku:
        print("Liian suuri")
        luku = int(input("Arvaa luku"))
print("Arvasit oikein!")

