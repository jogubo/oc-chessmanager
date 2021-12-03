from models import menu
from views import menu_view
from controllers import home_menu_ctrl
from controllers.new_tournament_ctrl import NewTournamentCtrl
from controllers.tournament_ctrl import TournamentCtrl


class TournamentMenuCtrl:
    def __init__(self):
        self.menu = menu.Menu()
        self.view = menu_view.MenuView(self.menu, "Tournois")

    def __call__(self):
        self.menu.add("auto", "Liste des tournois", None)
        self.menu.add("auto", "Créer un nouveau tournoi", TournamentCtrl().create_new())
        self.menu.add("auto", "Menu principal", home_menu_ctrl.HomeMenuCtrl())
        self.menu.add("Q", "Quitter", quit())

        user_choice = self.view.user_choice()

        # DEBUG
        print(user_choice.controller)
        user_choice.controller()
