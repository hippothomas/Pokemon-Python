import time

from bo.Player import Player
from bo.Pokemon import Pokemon


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

    print("Bien le bonjour ! Bienvenue dans le monde magique des Pokémon! Mon nom est Chen !\n"
          "Les gens souvent m'appellent le Prof Pokémon ! Ce monde est peuplé de créatures du nom de Pokémon !\n"
          "Pour certains, les Pokémon sont des animaux domestiques, pour d'autres,\n"
          "ils sont un moyen de combattre. Pour ma part... L'étude des Pokémon est ma profession.\n")

    username = str(input("Tout d'abord, quel est ton nom ? "))

    print("OK! Ton nom est donc " + username + " ! \n"
                                               "Un tout nouveau monde de rêves, d'aventures et de Pokémon t'attend !\n")

    time.sleep(3)
    print("Des Pokémon sauvages infestent les hautes herbes !\n"
          "Il te faut un Pokémon pour te protéger... Choisis en un !\n")
    return username


def menuStarter(username):
    starter1 = Pokemon(43)  # Starter Mystherbe
    starter2 = Pokemon(147)  # Starter MiniDraco
    starter3 = Pokemon(60)  # Starter Ptitard
    starterArray = [starter1, starter2, starter3]

    print("╔══════════════════════════════╗")
    print("╠═══════ CHOIX STARTER ════════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    for i in range(len(starterArray)):
        print("║" + " " * 4 + str(i + 1) + " - " + starterArray[i].nom + " " * (
                22 - len(str(starterArray[i].nom))) + "║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    pokeChoose = False
    while not pokeChoose:
        try:
            starterChoice = int(input("Quel pokémon voulez vous choisir : "))
            if starterChoice > 3 or starterChoice <= 0:
                raise Exception()
            else:
                pokeChoose = True
        except:
            print("\nVeuillez choisir un pokémon valide")
    print("\nSuper ! tu as choisis " + starterArray[starterChoice - 1].nom + " prend en soin !\n")
    player = Player(username)
    player.addPokeList(starterArray[starterChoice - 1])
    player.addPokedex(starterArray[starterChoice - 1])
    return player
