class Player:
    username = ""
    poke_list = []
    item_list = []
    pokedex = []

    def __init__(self, username):
        self.username = username

    def setPokeList(self, pokemon):
        self.poke_list.append(pokemon)

