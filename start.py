import menu.menu as menu
import bo.Pokemon as poke

starter1 = poke.Pokemon(43)  # Starter Mystherbe
starter2 = poke.Pokemon(147)  # Starter MiniDraco
starter3 = poke.Pokemon(60)  # Starter Ptitard

starter_arr = [starter1, starter2, starter3]

menu.menuDialogueStart()
starter = menu.menuStarter(starter_arr)