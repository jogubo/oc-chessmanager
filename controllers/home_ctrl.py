from models.menu import Menu
from views.menu_view import MenuView
from controllers.tournament_ctrl import TournamentCtrl
from controllers.players_ctrl import PlayersCtrl


class HomeCtrl:

    menu = Menu()
    view = MenuView(menu, "Menu principal")

    @classmethod
    def display_menu(cls):
        cls.menu.add(
                "auto",
                "Créer un nouveau tournoi",
                TournamentCtrl.create_new
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
                TournamentCtrl.create_new
                )
        user_choice = cls.view.user_choice()
        user_choice.controller()
