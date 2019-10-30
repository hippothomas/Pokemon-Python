import json

from bo.Player import Player
from bo.Pokemon import Pokemon


def loadPlayer():
    with open("./json/user.json") as json_file:
        data = json.load(json_file)
        player = Player(data["username"])
        pokelist = data["poke_list"]
        for poke_id in pokelist:
            Pokemon(poke_id)
        print(player.username)
        print(pokelist)
