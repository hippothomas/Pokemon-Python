class Player:
    username = ""
    poke_list = []
    item_list = []
    pokedex = []

    def __init__(self, username):
        self.username = username

    def addPokeList(self, pokemon):
        self.poke_list.append(pokemon)

    def addPokedex(self, pokemon):
        self.pokedex.append(pokemon)

