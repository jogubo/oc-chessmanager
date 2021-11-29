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
                [[1, 3, 4], [2, 6, 12], [3, 6, 15], [6, 12, 1]],
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

    def generate_pvp(self):
        players = self._tournament.players
        print(f"Liste avant algo: {players}")
        score = 1
        rank = 2
        players.sort(key=lambda x: x[score], reverse=True)
        for i in range(0, len(players)):
            for j in range(0, len(players)-i-1):
                if (players[j][score] == players[j+1][score]):
                    if (players[j][rank] > players[j+1][rank]):
                        temp = players[j]
                        players[j] = players[j+1]
                        players[j+1] = temp

        print(f"Liste triée: {players}")
        return players

    def test(self):
        print(self._players)
