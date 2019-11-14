# import menu.MenuStart
# import menu.MenuMain
# import bo.Pokemon as poke
# from bo.Player import Player
#
# starter1 = poke.Pokemon(43)  # Starter Mystherbe
# starter2 = poke.Pokemon(147)  # Starter MiniDraco
# starter3 = poke.Pokemon(60)  # Starter Ptitard
#
# starter_arr = [starter1, starter2, starter3]
#
# username = menu.MenuStart.menuDialogueStart()
# player = Player(username)
# starter = menu.MenuStart.menuStarter(username)
# menu.MenuMain.menuMain(player)
from services import playerJson

player = playerJson.loadPlayer()
print(player.poke_list[0].nom)
print(player.poke_list[1].nom)
playerJson.savePlayer(player)