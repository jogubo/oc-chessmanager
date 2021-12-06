from models.menu import Menu
from views.menu_view import MenuView


class HomeCtrl:

    menu = Menu()
    view = MenuView(menu, "Menu principal")

    @classmethod
    def display_menu(cls):
        cls.menu.add(
                "1",
                "Créer un nouveau tournoi",
                'new_tournament'
                )
        cls.menu.add(
                "2",
                "Liste des joueurs",
                'list_players'
                )
        cls.menu.add(
                "3",
                "Ajouter un nouveau joueur", 'new_player'
                )

        cls.menu.add(
                "Q",
                "Quitter",
                'close_app'
                )
        user_choice = cls.view.user_choice()
        return user_choice.controller
