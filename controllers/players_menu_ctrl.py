from models import menu
from views import menu_view
from controllers import home_menu_ctrl
from controllers import players_ctrl
from controllers import new_player_ctrl


class PlayersMenuCtrl:
    def __init__(self):
        self.menu = menu.Menu()
        self.view = menu_view.MenuView(self.menu, "Joueurs")

    def __call__(self):
        self.menu.add("auto", "Liste des joueurs", players_ctrl.PlayerCtrl())
        self.menu.add("auto", "Ajouter un nouveau joueur", new_player_ctrl.NewPlayerCtrl())
        self.menu.add("auto", "Menu principal", home_menu_ctrl.HomeMenuCtrl())
        self.menu.add("Q", "Quitter", None)

        user_choice = self.view.user_choice

        # DEBUG
        print(user_choice.controller)
        user_choice.controller()
