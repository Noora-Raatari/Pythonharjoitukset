import mysql.connector
def hae_kentan_tiedot(maakoodi):
    sql = (f"SELECT type, COUNT(*) FROM airport where iso_country = '{maakoodi}' GROUP BY type desc")
    print (sql)
    kursori =yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if kursori.rowcount > 0:
      for i in tulos:
          print (f" {i}")
    else:
        print ("maakoodillasi ei löytynyt lentoasemaa")

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='noora',
         password='käyttäjä',
         autocommit=True
         )
lentokenttä = input("Anna maakoodi: ")
hae_kentan_tiedot(lentokenttä)