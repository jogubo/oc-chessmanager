from views.tournament_form_view import TournamentFormView
from controllers import tournament_menu_ctrl
from models.tournament import Tournament
from models.player import Player
from utils.database import Database


class NewTournamentCtrl:
    def __call__(self):
        menu = tournament_menu_ctrl.TournamentMenuCtrl()
        new_tournament_form = TournamentFormView("Créer un nouveau tournoi")
        form = new_tournament_form.new()
        tournament = None
        menu()
