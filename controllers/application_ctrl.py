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
        'list_tournaments': {
            'title': "Liste des tournois",
            'controller': TournamentsCtrl.list_tournaments
            },
        'get_tournament': {
            'title': "",
            'controller': TournamentsCtrl.get_tournament
            },
        'tournament_ranking': {
            'title': "",
            'controller': TournamentsCtrl.get_ranking
            },
        'next_round': {
            'title': "",
            'controller': TournamentsCtrl.get_next_round
            },
        'set_score': {
            'title': "",
            'controller': TournamentsCtrl.set_score
            },
        'list_rounds': {
            'title': "",
            'controller': TournamentsCtrl.list_rounds
            },
        'new_tournament': {
            'title': "Créer un nouveau tournoi",
            'controller': TournamentsCtrl.create_new
            },
        'list_players': {
            'title': "Liste des joueurs",
            'controller': PlayersCtrl.list_players
            },
        'sort_players': {
            'title': "",
            'controller': PlayersCtrl.sort_list_players
            },
        'get_player': {
            'title': "Fiche du joueur",
            'controller': PlayersCtrl.get_player
            },
        'change_player_rank': {
            'title': "Modifier le classement du joueur",
            'controller': PlayersCtrl.change_player_rank
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
        self.parameters = None
        self.title = self.ROUTES[self.route]['title']
        self.close_app = None

    def controller(self, parameters):
        parameters = parameters
        controller_method = self.ROUTES[self.route]['controller']
        if parameters is None:
            next_route, next_parameters = controller_method()
        else:
            kwargs = parameters
            next_route, next_parameters = controller_method(**kwargs)
        self.route = next_route
        self. parameters = next_parameters

    def run(self):
        while True:
            self.controller(self.parameters)
