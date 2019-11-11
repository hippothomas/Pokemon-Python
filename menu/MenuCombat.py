import random

from bo.Item import Item
from menu import MenuMain as MenuMain


class MenuCombat:

    def __init__(self):
        None

def menuCombat(player):
    choice1 = "Combattre"
    choice2 = "Inventaire"
    choice3 = "Changer de pokémon"
    choice4 = "Fuir"

    getChoice = [choice1,
                 choice2,
                 choice3,
                 choice4]

    print("\n╔══════════════════════════════╗")
    print("╠═══════ MENU COMBATTRE ═══════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    print("║   1 - Combattre              ║")
    print("║   2 - Inventaire             ║")
    print("║   3 - Changer de pokémon     ║")
    print("║   4 - Fuir                   ║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    menuChoose = False
    while not menuChoose:
        try:
            menuChoice = int(input("Quel action voulez-vous faire : "))
            if menuChoice > 4 or menuChoice <= 0:
                raise Exception()
            else:
                menuChoose = True
        except:
            print("\nVeuillez choisir une action valide")
    print("\nTu as choisi l'option : " + str(getChoice[menuChoice - 1]))

    if (menuChoice == 1):
        print("lul")

    elif (menuChoice == 2):
        menuInventaireCombat(player)

    elif (menuChoice == 3):
        print("lul")

    elif (menuChoice == 4):
        MenuMain.menuMain(player)


def menuInventaireCombat(player):
    print("\n╔══════════════════════════════╗")
    print("╠═════════ INVENTAIRE ═════════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    i = 0
    for item in player.getInventaire():
        item_name = Item(item[1]).name
        print("║   " + str(i + 1) + " - " + str(item[0]) + "x" + item_name + "           ")
        i += 1
    print("║                              ║")
    print("║   1 - Utiliser un objet      ║")
    print("║   2 - Quitter                ║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

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