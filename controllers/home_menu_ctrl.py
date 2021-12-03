from models import menu
from views import menu_view
from controllers.tournament_menu_ctrl import TournamentMenuCtrl
from controllers.players_menu_ctrl import PlayersMenuCtrl
from controllers.tournament_ctrl import TournamentCtrl
from controllers.players_ctrl import PlayersCtrl


class HomeMenuCtrl:
    def __init__(self):
        self._menu = menu.Menu()
        self._view = menu_view.MenuView(self._menu, "Menu principal")

    def __call__(self):
        self._menu.add("auto", "Tournois", TournamentMenuCtrl())
        self._menu.add("auto", "Joueurs", PlayersMenuCtrl())
        self._menu.add("auto", "Quitter", TournamentCtrl.create_new)
        self._menu.add("auto", "Liste des joueurs", PlayersCtrl())

        user_choice = self._view.user_choice()

        # DEBUG
        # print(user_choice.controller)
        user_choice.controller()
