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
                'controller': PlayersCtrl.get_list_players
                },
            'new_player': {
                'title': "Ajouter un nouveau joueur",
                'controller': PlayersCtrl.create_new
                },
            'close_app': {
                'title': "Fermer l'application",
                'controller': sys.exit
                }
            }

    def __init__(self):
        self.route = 'home'
        self.title = self.ROUTES[self.route]['title']
        self.close_app = False

    def run(self):
        while True:
            controller_method = self.ROUTES[self.route]['controller']
            next_route = controller_method()
            self.route = next_route
            self.title = self.ROUTES[next_route]['title']
