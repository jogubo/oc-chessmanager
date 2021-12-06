from utils.database import Database
from models.tournament import Tournament
from controllers.players_ctrl import PlayersCtrl
from views.tournaments_view import TournamentsView


class TournamentsCtrl:
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

    @staticmethod
    def create_new():
        form = TournamentsView.create_new_tournament()
        players, ids = [], []
        total_players = form["nb_players"]
        while total_players > 0:
            player = PlayersCtrl.search_by_name()
            if player["id"] in ids:
                continue
            players.append((player["id"], 0.0, player["rank"], []))
            ids.append(player["id"])
            total_players -= 1
        tournament = Tournament(
                form["name"],
                form["description"],
                form["location"],
                players,
                form["date"],
                "turns",
                "rounds",
                "Blitz",
                )
        serialized_tournaments = []
        serialized_tournaments.append(tournament.serialize())
        Database.add('tournaments', serialized_tournaments)
        return 'home'
