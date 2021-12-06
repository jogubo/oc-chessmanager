import sys
from controllers.home_ctrl import HomeCtrl
from controllers.tournaments_ctrl import TournamentsCtrl
from controllers.players_ctrl import PlayersCtrl


class ApplicationCtrl:

    ROUTES = {
            'home': {
                'title': "Menu Principal",
                'controller': HomeCtrl.display_menu
                },
            'new_tournament': {
                'title': "Créer un nouveau tournoi",
                'controller': TournamentsCtrl.create_new
                },
            'list_players': {
                'title': "Liste des joueurs",
                'controller': PlayersCtrl.get_list
                },
            'new_player': {
                'title': "Ajouter un nouveau joueur",
                'controller': PlayersCtrl.create_new
                }
            }

    def __init__(self):
        self.route = 'home'
        self.close_app = False

    def start(self):
        while not self.close_app:
            controller_method = self.ROUTES[self.route]['controller']
            next_route = controller_method()
            self.route = next_route
            if next_route == 'close_app':
                self.close_app = True
                sys.exit()
