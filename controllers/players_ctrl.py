from utils. database import Database
from models.player import Player
from views.players_view import PlayersView


class PlayerCtrl:

    def __init__(self):
        self._view = PlayersView("Liste des joueurs")

    def __call__(self):
        serialized_players = Database.get('players')
        players = []
        for player in serialized_players:
            player = Player(
                    first_name=player["first_name"],
                    last_name=player["last_name"],
                    birth=player["birth"],
                    civility=player["civility"],
                    rank=player["rank"],
                    id=player["id"]
                    )
            players.append(player)
        self._view.list(players)

    def search(self):
        '''
        Search a player by name
        '''
        search_result = Database.search('players', self._view.search())
        players = []
        for player in search_result:
            player = Player(
                    first_name=player["first_name"],
                    last_name=player["last_name"],
                    birth=player["birth"],
                    civility=player["civility"],
                    rank=player["rank"],
                    id=player["id"]
                    )
            players.append(player)
        player = self._view.list(players)
        player = players[int(player) - 1]
        return player.id
