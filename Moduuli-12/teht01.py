import json
import requests


pyyntö = "https://api.chucknorris.io/jokes/random" 

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        json.dumps(json_vastaus, indent=2)
        print("Here's a bad Chuck Norris joke:") 
        print(json_vastaus["value"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")