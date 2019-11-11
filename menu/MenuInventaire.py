from bo.Item import Item

class MenuInventaire:

    def __init__(self):
        None

def menuInventaire(player):
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
    print("╚══════════════════════════════╝\n")