from models.menu import Menu
from views.menu_view import MenuView
from controllers.tournaments_ctrl import TournamentsCtrl
from controllers.players_ctrl import PlayersCtrl


class HomeCtrl:

    menu = Menu()
    view = MenuView(menu, "Menu principal")

    @classmethod
    def display_menu(cls):
        cls.menu.add(
                "auto",
                "Créer un nouveau tournoi",
                TournamentsCtrl.create_new
                )
        cls.menu.add(
                "auto",
                "Liste des joueurs",
                PlayersCtrl()
                )
        cls.menu.add(
                "auto",
                "Ajouter un nouveau joueur", PlayersCtrl.create_new
                )

        cls.menu.add(
                "Q",
                "Quitter",
                None
                )
        user_choice = cls.view.user_choice()
        user_choice.controller()
