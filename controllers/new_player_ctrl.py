from views.player_form_view import PlayerFormView
from controllers import players_menu_ctrl
from models.player import Player
from utils.functions import open_db, save_db


class NewPlayerCtrl:
    def __call__(self):
        menu = players_menu_ctrl.PlayersMenuCtrl()
        new_player_form = PlayerFormView("Ajouter un nouveau joueur")
        form = new_player_form.new()
        player = Player(
                form['first_name'],
                form['last_name'],
                form['birth'],
                form['civility']
                )
        serialized_players = open_db('players')
        serialized_players.append(player.serialize)
        save_db('players', serialized_players)
        menu()
