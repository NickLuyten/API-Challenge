#modules imorteren
import requests
import urllib.parse
from tabulate import tabulate


#start variabelen aanmaken en read access token invullen
titel = ""
baseurl = "https://api.themoviedb.org/3/"
apiRaT = "API READ ACCESS TOKEN"
headers = {'Authorization': 'Bearer ' + apiRaT}

#Zoeken naar de film
while titel != "S":
    titel = input("Welke film wil je zoeken? (S)top")
    if titel == "S":
        break
    # url wordt samengesteld aan de hand van de baseurl + de search functie met als parameter de titel van een film dat je zoekt.
    url = baseurl + "search/movie?" + urllib.parse.urlencode({"query":titel})
    json_data = requests.get(url,headers=headers).json()

    print(url)
    #lijst met resultaten wordt iedere keer opnieuw gemaakt
    resultaat = []
    #voor elk resultaat dat er is wordt dit toegevoegd aan de lijst resultaten
    for result in json_data["results"]:
        resultaat.append([result["popularity"], result["id"], result["title"], result["release_date"]])
    #met behulp van tabulate worden de resultaten afgeprint in een tabel.
    print(tabulate(resultaat, headers=["populariteit", "id", "titel", "release datum"]))


