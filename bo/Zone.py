import json
import random

JSON_ZONE_PATH = "../json/zone.json"
NOMBRE_ZONES_JSON = 5
ID_VILLE = NOMBRE_ZONES_JSON - 1


class Zone:
    id = ""
    type = ""
    name = ""


class ZoneVille(Zone):
    list_item = []

    def __init__(self):
        self.id = ID_VILLE
        with open(JSON_ZONE_PATH) as jsonFile:
            data = json.load(jsonFile)
            self.type = data["zones"][self.id]["type"]
            self.name = data["zones"][self.id]["name"]
            self.list_item = data["zones"][self.id]["list_item"]


class ZonePokemon(Zone):
    list_pokemon_id = []

    def __init__(self):
        self.id = random.randrange(0, NOMBRE_ZONES_JSON - 1)
        with open(JSON_ZONE_PATH) as jsonFile:
            data = json.load(jsonFile)
            self.type = data["zones"][self.id]["type"]
            self.name = data["zones"][self.id]["name"]
            self.list_item = data["zones"][self.id]["list_pokemon_id"]


a = ZoneVille()
print(a.type)
print(a.name)
print(a.list_item)

print("\n \n")

b = ZonePokemon()
print(b.type)
print(b.name)
print(b.list_item)