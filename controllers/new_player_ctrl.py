from views.player_form_view import PlayerFormView
from controllers import players_menu_ctrl
from models.player import Player
from utils.functions import open_db, save_db


class NewPlayerCtrl:
    def __call__(self):
        self._menu = players_menu_ctrl.PlayersMenuCtrl()
        self._new_player_form = PlayerFormView("Ajouter un nouveau joueur")
        self._form = self._new_player_form.new()
        player = Player(
                self._form['first_name'],
                self._form['last_name'],
                self._form['birth'],
                self._form['civility']
                )
        serialized_players = open_db('players')
        serialized_players.append(player.serialize)
        save_db('players', serialized_players)
        self._menu()
