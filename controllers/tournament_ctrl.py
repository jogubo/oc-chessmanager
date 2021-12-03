from utils.database import Database
from models.tournament import Tournament
from controllers.players_ctrl import PlayersCtrl


class TournamentCtrl:
    def __init__(self, tournament_id):
        data = Database.get('tournaments', tournament_id)
        self._tournament = Tournament(
                data["name"],
                "location",
                data["players"],
                "date",
                "turns",
                "rounds",
                "time",
                "description"
                )

        self._players = {}
        for player in self._tournament.players_data:
            id = player[0]
            self._players[id] = PlayersCtrl.get_player(id)
            self._players[id].score = player[2]
            self._players[id].rank = player[3]
