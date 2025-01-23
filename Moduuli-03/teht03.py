sukupuoli = input("Anna biologinen sukupuoli")
veri= float (input("Anna hemoglobiiniarvo g/l"))

if (sukupuoli=='nainen' and 175>veri>=117) or (sukupuoli=='mies' and 195>veri>=134):
    print("Hemoglobiinisi on normaali")

elif (sukupuoli=='nainen' and veri<=117) or (sukupuoli=='mies' and veri<=134):
    print ("Hemoglobiinisi on alhainen")

elif (sukupuoli=='nainen' and veri>175) or (sukupuoli=='mies' and veri>195):
    print("Hemoglobiinisi on korkea")