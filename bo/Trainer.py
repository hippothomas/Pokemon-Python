class Trainer:
    name = ""
    poke_equipe = []

    def __init__(self, name):
        self.name = name
        self.poke_equipe = []

    def addPokeEquipe(self, pokemon):
        self.poke_equipe.append(pokemon)

