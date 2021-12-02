from utils.database import Database
from models.tournament import Tournament
from models.player import Player


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
            serialized_player = Database.get('players', id)
            player = Player(
                    first_name=serialized_player["first_name"],
                    last_name=serialized_player["last_name"],
                    birth=serialized_player["birth"],
                    civility=serialized_player["civility"],
                    rank=1,
                    id=serialized_player.doc_id
                    )
            self._players[id] = player
