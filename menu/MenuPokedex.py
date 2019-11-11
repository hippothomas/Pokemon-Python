from menu import MenuMain

class MenuPokedex:

    def __init__(self):
        None

def getPokedex(player):
    displayPokedex(1, 21, player)
    pageChoose = False
    while not pageChoose:
        try:
            print("Page 1|2|3|4|5|6|7|8\nQuitter 0")
            page = int(input("Choisir une option : "))
            if page > 3 or page < 0:
                raise Exception()
        except:
            print("Veuillez choisir une page valide")
        if page == 0:
            MenuMain.menuMain(player)
        elif page == 1:
            displayPokedex(1, 21, player)
        elif page == 2:
            displayPokedex(21, 41, player)
        elif page == 3:
            displayPokedex(41, 61, player)
        elif page == 4:
            displayPokedex(61, 81, player)
        elif page == 5:
            displayPokedex(81, 101, player)
        elif page == 6:
            displayPokedex(101, 121, player)
        elif page == 7:
            displayPokedex(121, 141, player)
        elif page == 8:
            displayPokedex(141, 151, player)

def displayPokedex(firstNum, lastNum, player):
    print("╔══════════════════════════════╗")
    print("╠════════ Votre pokedex ═══════╣")
    print("╠══════════════════════════════╣")
    for i in range(firstNum, lastNum):
        pokemon = pokemonIsFound(player.pokedex, i)
        print("║ " + str(i) + " : {}".format(
            "Nom : " + pokemon + " " * (
                    20 - (len(str(i)) + len(pokemon))) + "║"))
    print("╚══════════════════════════════╝\n")

def pokemonIsFound(pokedex, index):
    for i in range(len(pokedex)):
        if pokedex[i].id == index:
            return str(pokedex[i].nom)
        else:
            return "?"
