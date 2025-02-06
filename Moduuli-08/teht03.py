import geopy
import mysql.connector
def hae_kentan_tiedot(lentokenttä1):
    sql = (f"SELECT latitude_deg, longitude_deg from airport where ident= '{lentokenttä1}' ")
    #print (sql)
    kursori =yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if kursori.rowcount > 0:
      for rivi in tulos:
          loc1 = rivi[0], rivi [1]
          return loc1

    else:
        print ("maakoodillasi ei löytynyt lentoasemaa")

def hae_kentan_tiedot(lentokenttä2):
    sql = (f"SELECT latitude_deg, longitude_deg from airport where  ident= '{lentokenttä2}' ")
    #print (sql)
    kursori =yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if kursori.rowcount > 0:
      for rivi in tulos:
          loc2 = rivi [0], rivi[1]
          return loc2

    else:
        print ("ICAO koodillasi ei löytynyt lentoasemaa")


def laske_etäisyys (kenttä1,kenttä2):
    from geopy import distance
    etäisyys=(distance.distance(kenttä1,kenttä2).km)
    print (f"Valitsemiesi lentokenttien etäisyys on {etäisyys:.2f} km")

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='noora',
         password='käyttäjä',
         autocommit=True
         )
lentokenttä1 = input("Anna ICAO-koodi nro 1: ")
lentokenttä2= input ("Aanna ICAO-koodi nro 2:")
kenttä1 = hae_kentan_tiedot(lentokenttä1)
kenttä2 = hae_kentan_tiedot (lentokenttä2)
print (f"Kentän 1 koordinaatit {kenttä1}")
print (f"Kentän 2 koordinaatit {kenttä2}")
laske_etäisyys(kenttä1,kenttä2)




