from utils.database import Database
from models.player import Player


class TournamentCtrl:
    def __init__(self, tournament_id):
        self._players = []
        data = Database.get('tournaments', tournament_id)
        for id in data["players"]:
            serialized_player = Database.get('players', id-1)
            player = Player(
                    first_name=serialized_player["first_name"],
                    last_name=serialized_player["last_name"],
                    birth=serialized_player["birth"],
                    civility=serialized_player["civility"],
                    rank=serialized_player["rank"],
                    id=serialized_player.doc_id
                    )
            self._players.append(player)

    def test(self):
        print(self._players)
