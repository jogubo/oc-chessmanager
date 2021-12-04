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
                'new_tournament'
                )
        cls.menu.add(
                "auto",
                "Liste des joueurs",
                'list_players'
                )
        cls.menu.add(
                "auto",
                "Ajouter un nouveau joueur", 'new_player'
                )

        cls.menu.add(
                "Q",
                "Quitter",
                'close_app'
                )
        user_choice = cls.view.user_choice()
        return user_choice.controller
