hyttiluokka= input("Anna hyttiluokkasi")
if hyttiluokka=='lux' or hyttiluokka=='LUX':
    print("LUX on parvekkeellinen hytti yläkannella")
elif hyttiluokka=='A' or hyttiluokka=='a':
    print("A-hytti on ikkunallinen hytti autokannen yläpuolella")
elif hyttiluokka=='B' or hyttiluokka=='b':
    print ("B-hytti on ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka=='C' or hyttiluokka=='c':
    print ("C-hytti on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")