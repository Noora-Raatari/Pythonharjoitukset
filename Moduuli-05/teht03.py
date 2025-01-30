alkuluku=True
luku = int(input("Anna kokonaisluku"))

for n in range (2,luku):
    if luku%n == 0:
        alkuluku= False
    break

if alkuluku:
    print("lukusi on alkuluku")
else:
    print ("lukusi ei ole alkuluku")