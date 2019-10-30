import random
import time

from bo.Item import Item


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

    time.sleep(5)
    print("Des Pokémon sauvages infestent les hautes herbes! \n"
          "Il te faut un Pokémon pour te protéger... Choisis en un ! \n")
    time.sleep(5)


def menuStarter(starter):
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
    return starter[starterChoice - 1]


def menuInventaire(player):
    print("╔==============================╗")
    print("║========= INVENTAIRE =========║")
    print("║==============================║")
    print("║                              ║")
    i = 0
    for item in player.getInventaire():
        item_name = Item(item[1]).name
        print("║   " + str(i + 1) + " - " + str(item[0]) + "x" + item_name + "           ")
        i += 1
    print("║                              ║")
    print("║   1 - Utiliser un item       ║")
    print("║   2 - Quitter                ║")
    print("║                              ║")
    print("╚==============================╝\n")

    # L'utilisateur fait un choix
    choose = False
    while not choose:
        try:
            inputChoice = int(input("Votre choix: "))
            if inputChoice == 1 or inputChoice == 2:
                choose = True
            else:
                raise Exception()
        except:
            print("Veuillez faire un choix valide")

    if inputChoice == 1:
        # L'utilisateur choisi quel item utiliser
        chooseItem = False
        while not chooseItem:
            try:
                chooseItemId = int(input("Veuillez choisir un item : "))
            except:
                print("La saisie n'est pas valide !")
                chooseItemId = -1

            # Si l'item est bien dans l'inventaire
            if player.existInventaire(chooseItemId):
                chooseItem = True
                inventaire = player.getInventaire()
                item = Item(inventaire[chooseItemId - 1][1])
                # Si l'item est de type pokeball
                if item.type == 1:
                    rnd = random.randint(0, 100);
                    # Test si la capture du pokémon est efficace
                    if rnd <= item.effect:
                        # Réussite
                        print("Votre " + item.name + " est très éfficace !")
                        print("Vous venez de capturer ...")
                        # player.addPokeList(enemy)
                    else:
                        # Echec
                        print("Votre " + item.name + " n'est très pas éfficace...")
                    # Passe le tour du joueur en cours
                # Si l'item est de type potion
                elif item.type == 2:
                    print("Vous utilisez " + item.name + "...")
                    # oldhp = pokemon.hp
                    # if (pokemon.hp + item.effect) >= 100:
                    #    pokemon.hp = 100
                    # else:
                    #    pokemon.hp += item.effect
                    # print("Votre pokémon vient de gagné " + str(pokemon.hp - oldhp) + "hp grâce à " + item.name)

                # On retire 1 à la quantité de l'item utilisé
                player.useInventaire(chooseItemId - 1)
            else:
                print("Erreur ! L'item demandé n'existe pas !")
