import requests

url = "https://www.wikidata.org/w/api.php"

#query = input("digite a pesquisa: ")

params = {
        "action" : "wbsearchentities",
        "language" : "pt",
        "format" : "json",
        "search" : "python"
}

data = requests.get(url, params=params)

sl = "pt-br"
tl = "en"
operation = "translate"

text = data.json()["search"][0]["description"]

from googletrans import Translator
#print(type(text))

translator = Translator()

print(translator.translate('big moon', src='en', dest='pt').text)

    