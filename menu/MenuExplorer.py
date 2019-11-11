from bo.Zone import ZoneVille, ZonePokemon
from menu import MenuCombat as MenuCombat
from menu import MenuMain as MenuMain

class MenuExplorer:

    def __init__(self):
        None

def menuExplorer(player):
    choice1 = "Changer de zone"
    choice2 = "Aller en ville"
    choice3 = "Chasser des pokémons"
    choice4 = "Combattre un dresseur"
    choice5 = "Menu principal"

    getChoice = [choice1,
                 choice2,
                 choice3,
                 choice4,
                 choice5]

    print("\n╔══════════════════════════════╗")
    print("╠══════ MENU EXPLORATION ══════╣")
    print("╠══════════════════════════════╣")
    print("║                              ║")
    print("║   1 - Changer de zone        ║")
    print("║   2 - Aller en Ville         ║")
    print("║   3 - Chasser des pokémons   ║")
    print("║   4 - Combattre un dresseur  ║")
    print("║   5 - Menu principal         ║")
    print("║                              ║")
    print("╚══════════════════════════════╝\n")

    menuChoose = False
    while not menuChoose:
        try:
            menuChoice = int(input("Quel action voulez-vous faire : "))
            if menuChoice > 5 or menuChoice <= 0:
                raise Exception()
            else:
                menuChoose = True
        except:
            print("\nVeuillez choisir une action valide")
    print("\nTu as choisi l'option : " + str(getChoice[menuChoice - 1]))

    if (menuChoice == 1):
        zone = ZonePokemon()
        print("\nVous arrivez dans la zone : " + str(zone.name) + "\n")
        menuExplorer(player)

    elif (menuChoice == 2):
        zone = ZoneVille()
        print("\nVous arrivez dans la zone : " + str(zone.name) + "\n")
        MenuMain.menuMain(player)

    elif (menuChoice == 3):
        zone = ZonePokemon()
        zone.getRandomPokemonByZone()
        MenuCombat.menuCombat(player)

    elif (menuChoice == 4):
        zone = ZonePokemon()
        zone.getRandomDresseurByZone()
        MenuCombat.menuCombat(player)

    elif (menuChoice == 5):
        MenuMain.menuMain(player)