from controllers.home_ctrl import HomeCtrl
from controllers.tournament_ctrl import TournamentCtrl


class Application:


    def __call__(self):
        HomeCtrl.display_main_menu()
