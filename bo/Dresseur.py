class Dresseur:
    name = ""
    poke_list = []

    def __init__(self, name):
        self.name = name
        self.poke_list = []

    def addPokeList(self, pokemon):
        self.poke_list.append(pokemon)
