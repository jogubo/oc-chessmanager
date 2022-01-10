from views.home_view import HomeView


class HomeCtrl:

    @staticmethod
    def display_menu():
        menu = {
            '1':
            {
                'menu_title': "Liste des tournois",
                'route': ('list_tournaments', {'display': 'all'})
            },
            '2':
            {
                'menu_title': "Liste des joueurs",
                'route': ('list_players', {'display': 'all'})
            },
            'Q':
            {
                'menu_title': "Quitter",
                'route': ('close_app', None)
            }
        }
        user_choice = HomeView.display_menu(menu)
        return user_choice
