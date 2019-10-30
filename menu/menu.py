import time

from bo.Player import Player


def menuDialogueStart():
    print("                                  ,'\\\n"
          "    _.----.        ____         ,'  _\   ___    ___     ____\n"
          "_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.\n"
          "\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |\n"
          " \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |\n"
          "   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n"
          "    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |\n"
          "     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |\n"
          "      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |\n"
          "       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n"
          "        \_.-'       |__|    `-._ |              '-.|     '-.| |   |\n"
          "                                `'                            '-._|\n")
    print("Bien le bonjour! Bienvenue dans le monde magique des Pokémon! Mon nom est Chen! \n"
          "Les gens souvent m'appellent le Prof Pokémon! Ce monde est peuplé de créatures du nom de Pokémon! \n"
          "Pour certains, les Pokémon sont des animaux domestiques, pour d'autres, \n"
          "ils sont un moyen de combattre. Pour ma part... L'étude des Pokémon est ma profession. \n")
    username = str(input("Tout d'abord, quel est ton nom ? "))

    print("OK! Ton nom est donc " + username + " ! \n"
          "Un tout nouveau monde de rêves, d'aventures et de Pokémon t'attend! \n\n")

    time.sleep(2)
    print("Des Pokémon sauvages infestent les hautes herbes! \n"
          "Il te faut un Pokémon pour te protéger... Choisis en un ! \n")
    return username

def menuStarter(starter, player):
    for i in range(len(starter)):
        print(str(i + 1) + " - " + starter[i].nom)
    pokeChoose = False
    while not pokeChoose:
        try:
            starterChoice = int(input("Quel pokémon voulez vous choisir : "))
            if starterChoice > 3 or starterChoice <= 0:
                raise Exception()
            else:
                pokeChoose = True
        except:
            print("Veuillez choisir un pokémon valide")
    print("Super ! tu as choisis " + starter[starterChoice - 1].nom + " prend en soin !")
    player.addPokeList(starter[starterChoice - 1])
    return starter[starterChoice - 1]

def getEquipe(player):
    print("╔═════════════════════════════════════════════════════════╗")
    print("╠═════════════════ Votre equipe de pokemon ═══════════════╣")
    print("╠═════════════════════════════════════════════════════════╣")
    for i in range(len(player.poke_list)):
        print("║ " + str(i+1) + " : {}".format("Nom : " + player.poke_list[i].nom + " | HP : " + str(player.poke_list[i].hp) + " | Niveau : " + str(player.poke_list[i].level)) + " " * (22 - len(player.poke_list[i].nom)) + "║")
    print("╚═════════════════════════════════════════════════════════╝\n")


