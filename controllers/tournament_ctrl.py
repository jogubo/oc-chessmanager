from utils.database import Database
from models.tournament import Tournament
from models.player import Player


class TournamentCtrl:
    def __init__(self, tournament_id):
        data = Database.get('tournaments', tournament_id)
        self._tournament = Tournament(
                data["name"],
                "location",
                # data["players"],
                #[[1, 0, 4], [7, 3, 3], [10, 0, 10], [2, 0, 12], [3, 1, 15], [6, 0, 1]],
                [[1, 0, 4, [7]], [7, 3, 3, [1]], [10, 0, 10, [3]], [2, 0, 12, [6]], [3, 1, 15, [10]], [6, 0, 1, [2]]],
                #[[1, 0, 4, [7, 6]], [7, 3, 3, [1, 3]], [10, 0, 10, [3, 2]], [2, 0, 12, [6, 10]], [3, 1, 15, [10, 7]], [6, 0, 1, [2, 1]]],
                "date",
                "turns",
                "rounds",
                "time",
                "description"
                )

        #self._players = []
        #for player in self._tournament.players:
        #    id = player[0]
        #    serialized_player = Database.get('players', id)
        #    player = Player(
        #            first_name=serialized_player["first_name"],
        #            last_name=serialized_player["last_name"],
        #            birth=serialized_player["birth"],
        #            civility=serialized_player["civility"],
        #            rank=serialized_player["rank"],
        #            id=serialized_player.doc_id
        #            )
        #    self._players.append(player)

    def test(self):
        print(f"Liste des joueurs : {self._tournament.players}")
        players = self._tournament.sort_players()
        print(f"Liste triée {players}")
        vs = self._tournament.generate_versus()
        print(f"Versus : {vs}")
