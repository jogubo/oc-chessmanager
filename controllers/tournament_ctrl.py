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
                [[1, 0, 4], [7, 3, 3], [10, 0, 10], [2, 0, 12], [3, 1, 15], [6, 0, 1]],
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

    def sort_players(self):
        '''
        Player's data is list:
            [player_id, player_score, player_rank]
        '''
        players = self._tournament.players
        score, rank = 1, 2
        players.sort(key=lambda x: x[score], reverse=True)
        for i in range(0, len(players)):
            for j in range(0, len(players)-i-1):
                if (players[j][score] == players[j+1][score]):
                    if (players[j][rank] > players[j+1][rank]):
                        temp = players[j]
                        players[j] = players[j+1]
                        players[j+1] = temp
        self._players = players
        return players

    def generate_versus(self):
        players = self._players
        median = int(len(players) / 2)
        versus = []
        if len(players[0]) == 3:
            for i in range(median):
                versus.append((players[i], players[i+median]))
                players[i].append([players[i+median][0]])
                players[i+median].append([players[i][0]])
        else:
            pass
        return versus

    def test(self):
        print(f"Liste des joueurs : {self._tournament.players}")
        players = self.sort_players()
        print(f"Liste triée {players}")
        vs = self.generate_versus()
        print(f"Versus : {vs}")
