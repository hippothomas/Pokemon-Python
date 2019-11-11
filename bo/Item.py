import requests


class Item:
    id = 0
    name = ""
    desc = ""
    cost = 0
    type = 0
    effect = 0

    apiUrl = "https://pokeapi.co/api/v2/"
    getItem = str(apiUrl) + "item/"

    def __init__(self, id):
        self.id = id
        item_json = requests.get(self.getItem + str(id)).json()
        # En fonction de la langue on récupère le nom et la description
        for it in item_json["names"]:
            if it["language"]["name"] == "fr":
                self.name = it["name"]
        for it in item_json['flavor_text_entries']:
            if it["language"]["name"] == "fr":
                self.desc = it["text"]

        self.cost = item_json['cost']

        # Si ce sont des pokéball
        if self.id == 4 or self.id == 3 or self.id == 2:
            self.type = 1
        # Si ce sont des potions
        elif self.id == 17 or self.id == 26 or self.id == 25:
            self.type = 2

        # On leur attribut un effet
        if self.id == 4: # Pokéball
            self.effect = 40
        elif self.id == 3: # Superball
            self.effect = 60
        elif self.id == 2: # Ultraball
            self.effect = 80
        elif self.id == 17: # Potion
            self.effect = 25
        elif self.id == 26: # Super Potion
            self.effect = 50
        elif self.id == 25: # Hyper Potion
            self.effect = 75
