from views.player_form_view import PlayerFormView
from controllers import players_menu_ctrl
from models.player import Player
from utils.functions import open_db, save_db


class NewPlayerCtrl:
    def __call__(self):
        self._menu = players_menu_ctrl.PlayersMenuCtrl()
        self._player_form = PlayerFormView("Ajouter un nouveau joueur")
        self._form = self._player_form.new()
        self._player = Player(
                self._form['first_name'],
                self._form['last_name'],
                self._form['birth'],
                self._form['civility']
                )
        # self._players = open_players_db()
        print(self._player.serialize)
        save_db('players', self._player.serialize)
        self._menu()
