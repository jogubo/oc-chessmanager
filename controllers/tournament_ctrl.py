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

        self._players = []
        for player in self._tournament.players:
            id = player[0]
            serialized_player = Database.get('players', id)
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
        self._tournament.players = [[1, 0, 4, []], [7, 0, 3, []], [10, 0, 10, []], [2, 0, 12, []], [3, 0, 15, []], [6, 0, 1, []]]
        print(f"Liste des joueurs : {self._tournament.players}\n")

        print("Tour 1")
        print(f"Liste triée {self._tournament.sort_players()}")
        vs = self._tournament.generate_versus()
        print(f"Versus : {vs}\n")

        print("Tour 2")
        self._tournament.players = [[1, 1.0, 4, [3]], [7, 1.0, 3, [2]], [10, 0.0, 10, [6]], [2, 0.0, 12, [7]], [3, 0.0, 15, [1]], [6, 1.0, 1, [10]]]
        print(f"Liste triée {self._tournament.sort_players()}")
        vs = self._tournament.generate_versus()
        print(f"Versus : {vs}\n")

        print("Tour 3")
        self._tournament.players = [[1, 2.0, 4, [3, 10]], [7, 1.0, 3, [2, 6]], [10, 0.0, 10, [6, 1]], [2, 0.5, 12, [7, 3]], [3, 0.5, 15, [1, 2]], [6, 2.0, 1, [10, 7]]]
        print(f"Liste triée {self._tournament.sort_players()}")
        vs = self._tournament.generate_versus()
        print(f"Versus : {vs}\n")
