import json
import requests

kaupunki = input("Anna paikkakunnan nimi: ")

pyyntö = (f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=2&appid=6290e96af85dc6548499de4c0deebaaa&lang=fi") 

try:
    vastaus01 = requests.get(pyyntö)
    if vastaus01.status_code==200:
        json_vastaus01 = vastaus01.json()

        if len(json_vastaus01) > 0:
            ensimmäinen_hakutulos= json_vastaus01[0]
            lat=(ensimmäinen_hakutulos["lat"])
            lon=(ensimmäinen_hakutulos["lon"])
        else:
            print("hakusanallasi ei löytynyt mitään")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")


sää_pyyntö = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=6290e96af85dc6548499de4c0deebaaa&lang=fi&units=metric")



try:
    vastaus02 = requests.get(sää_pyyntö)
    if vastaus02.status_code==200:
        json_vastaus02 = vastaus02.json()
        print ("lämpötila:",json_vastaus02["main"]["temp"],"astetta celsiusta")
        print ("säätilan kuvaus:",json_vastaus02 ["weather"][0]["description"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
