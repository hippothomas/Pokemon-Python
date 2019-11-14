from bo.Player import Player
from bo.Item import Item


def menuAchat(player):
    pokeball = Item(4)
    superball = Item(3)
    ultraball = Item(2)
    potion = Item(17)
    superpotion = Item(26)
    hyperpotion = Item(25)

    print("\n╔══════════════════════════════╗")
    print("╠══════════ BOUTIQUE ══════════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    print("║   1 - " + pokeball.name + " - " + str(pokeball.cost))
    print("║   2 - " + superball.name + " - " + str(superball.cost))
    print("║   3 - " + ultraball.name + " - " + str(ultraball.cost))
    print("║   4 - " + potion.name + " - " + str(potion.cost))
    print("║   5 - " + superpotion.name + " - " + str(superpotion.cost))
    print("║   6 - " + hyperpotion.name + " - " + str(hyperpotion.cost))
    print("║                              ║")
    print("║   7 - Quitter                ║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    # L'utilisateur fait un choix
    choose = False
    while not choose:
        try:
            inputChoice = int(input("Votre choix: "))
            if 1 <= inputChoice <= 7:
                choose = True
            else:
                raise Exception()
        except:
            print("Veuillez faire un choix valide")

    if inputChoice == 1:
        item = pokeball
    elif inputChoice == 2:
        item = superball
    elif inputChoice == 3:
        item = ultraball
    elif inputChoice == 4:
        item = potion
    elif inputChoice == 5:
        item = superpotion
    elif inputChoice == 6:
        item = hyperpotion

    if player.monnaie >= item.cost:
        player.monnaie -= item.cost
        player.addInventaire(item)

        print("Vous venez d'acheter : " + item.name)
        print("Il vous reste : " + str(player.monnaie))
    else:
        print("Vous n'avez pas assez d'argent !")
