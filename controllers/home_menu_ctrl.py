from models import menu
from views import menu_view
from controllers.tournament_menu_ctrl import TournamentMenuCtrl
from controllers.players_menu_ctrl import PlayersMenuCtrl


class HomeMenuCtrl:
    def __init__(self):
        self.menu = menu.Menu()
        self.view = menu_view.MenuView(self.menu, "Menu principal")

    def __call__(self):
        self.menu.add("auto", "Tournois", TournamentMenuCtrl())
        self.menu.add("auto", "Joueurs", PlayersMenuCtrl())
        self.menu.add("Q", "Quitter", None)

        user_choice = self.view.user_choice

        # DEBUG
        print(user_choice.controller)
        user_choice.controller()
