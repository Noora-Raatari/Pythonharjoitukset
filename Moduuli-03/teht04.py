vuosiluku_str =(input("Anna vuosiluku"))

vuosi = float (vuosiluku_str)
if vuosi%400==0 or vuosi%4==0:
    print("Vuosi on karkausvuosi")

else:
    print("vuosi ei ole karkausvuosi")