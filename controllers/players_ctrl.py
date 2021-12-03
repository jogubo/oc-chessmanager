from utils. database import Database
from models.player import Player
from views.players_view import PlayersView


class PlayersCtrl:

    def __init__(self):
        self._view = PlayersView("Liste des joueurs")

    def __call__(self):
        serialized_players = Database.get('players')
        for player in serialized_players:
            player["id"] = player.doc_id
        players = self.list(serialized_players)
        self._view.list(players)
        pass

    @staticmethod
    def get_player(id):
        data = Database.get('players', id)
        return Player(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    birth=data["birth"],
                    civility=data["civility"],
                    rank=data["rank"],
                    id=data.doc_id
                )

    def search(self):
        '''
        Search a player by name
        '''
        search_result = Database.search('players', self._view.search())
        players = self.list(search_result)
        user_choice = self._view.list(players)
        player = players[int(user_choice) - 1]
        return player.serialize

    def list(self, results):
        players = []
        for player in results:
            player = Player(
                    first_name=player["first_name"],
                    last_name=player["last_name"],
                    birth=player["birth"],
                    civility=player["civility"],
                    rank=player["rank"],
                    id=player["id"]
                    )
            players.append(player)
        return players

    @staticmethod
    def new_player():
        pass
