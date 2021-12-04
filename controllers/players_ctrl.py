from utils. database import Database
from models.player import Player
from views.players_view import PlayersView
#from views.player_form_view import PlayerFormView


class PlayersCtrl:

    @classmethod
    def get_list(cls):
        view = PlayersView("Liste des joueurs")
        serialized_players = Database.get('players')
        for player in serialized_players:
            player["id"] = player.doc_id
        players = cls.list(serialized_players)
        view.list(players)
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
    def create_new():
        form = PlayersView.create_new_player()
        player = Player(
                form['first_name'],
                form['last_name'],
                form['birth'],
                form['civility']
                )
        serialized_players = []
        serialized_players.append(player.serialize)
        Database.add('players', serialized_players)
