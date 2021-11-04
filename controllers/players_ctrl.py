from views.player_form_view import PlayerFormView
from controllers import players_menu_ctrl


class PlayersCtrl:
    def __init__(self):
        self._add_player = PlayerFormView("Ajouter un nouveau joueur")
        self._back = players_menu_ctrl.PlayersMenuCtrl()

    def __call__(self):
        player = self._add_player.new()
        self._back()
