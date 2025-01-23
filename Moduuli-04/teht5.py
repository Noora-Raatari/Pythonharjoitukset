
käyttäjätunnus=input("Anna käyttäjätunnus")
salasana=input("Anna salasana")

kirjautumiskerrat=0

while (käyttäjätunnus !='python' or salasana!='rules'):
    kirjautumiskerrat = kirjautumiskerrat + 1

    if kirjautumiskerrat >5:
        print("Annoit väärän salasanan tai käyttäjätunnuksen liian monta kertaa")
        break

    if kirjautumiskerrat<5:
        print("Väärä käyttäjätunnus tai salasana")
        käyttäjätunnus = input("Anna käyttäjätunnus")
        salasana = input("Anna salasana")
else:
    print("Welcome boss")


