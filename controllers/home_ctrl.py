from models.entities.menu import Menu
from views.menu_view import MenuView


class HomeCtrl:

    menu = Menu()
    view = MenuView(menu, "Menu principal")

    @classmethod
    def display_menu(cls):
        cls.menu.add(
                '1',
                "Liste des tournois",
                ('list_tournaments', {'display': 'all'})
                )
        cls.menu.add(
                '2',
                "Créer un nouveau tournoi",
                ('new_tournament', None)
                )
        cls.menu.add(
                '3',
                "Liste des joueurs",
                ('list_players', {'display': 'all'})
                )
        cls.menu.add(
                '4',
                "Ajouter un nouveau joueur",
                ('new_player', None)
                )

        cls.menu.add(
                'Q',
                "Quitter",
                ('close_app', None)
                )
        user_choice = cls.view.user_choice()
        return user_choice.controller
