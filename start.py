import menu.menu as menu
import bo.Pokemon as poke
from bo.Trainer import Trainer
from bo.Player import Player
from menu.menu_combat_dresseur import combat
import services.playerJson as player_json

starter1 = poke.Pokemon(43)  # Starter Mystherbe
starter2 = poke.Pokemon(147)  # Starter MiniDraco
starter3 = poke.Pokemon(60)  # Starter Ptitard

starter_arr = [starter1, starter2, starter3]

#username = menu.menuDialogueStart()
#player = Player(username)
#starter = menu.menuStarter(starter_arr, player)
#menu.menuMain(player)
poke_adversaire = Trainer("Balkani le maire")
poke_adversaire.addPokeEquipe(starter1)
poke_adversaire.addPokeEquipe(starter2)
player = player_json.loadPlayer()
combat(player, poke_adversaire)