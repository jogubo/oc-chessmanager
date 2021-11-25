from views.tournament_form_view import TournamentFormView
from controllers import tournament_menu_ctrl
from controllers.players_ctrl import PlayersCtrl
from models.tournament import Tournament
from utils.database import Database


class NewTournamentCtrl:
    def __init__(self):
        self._players = PlayersCtrl()

    def __call__(self):
        menu = tournament_menu_ctrl.TournamentMenuCtrl()
        new_tournament_form = TournamentFormView("Créer un nouveau tournoi")
        form = new_tournament_form.new()
        players = []
        i = form["nb_players"]
        while i > 0:
            selected_player = self._players.search()
            players.append(selected_player)
            i -= 1
        tournament = Tournament(
                form["name"],
                form["location"],
                players,
                "date",
                "turns",
                "rounds",
                "time",
                "description"
                )
        serialized_tournaments = []
        serialized_tournaments.append(tournament.serialize())
        Database.add('tournaments', serialized_tournaments)
        menu()
