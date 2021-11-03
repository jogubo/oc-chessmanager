from models import menu
from views import menu_view


class HomeMenuCtrl:
    def __init__(self):
        self.menu = menu.Menu()
        self.view = menu_view.MenuView(self.menu)

    def __call__(self):
        self.menu.add("auto", "Tournois", None)
        self.menu.add("auto", "Joueurs", None)
        self.menu.add("Q", "Quitter", None)

        user_choice = self.view.user_choice

        # DEBUG
        print(user_choice.controller)
        user_choice.controller()
