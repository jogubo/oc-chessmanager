from utils. database import Database
from models.player import Player
from views.players_view import PlayersView


class PlayersCtrl:

    @classmethod
    def get_list(cls):
        serialized_players = Database.get('players')
        for player in serialized_players:
            player["id"] = player.doc_id
        players = cls.create_list(serialized_players)
        print(serialized_players)
        PlayersView.list(players)
        return 'home'

    @staticmethod
    def get_player(player_id):
        data = Database.get('players', player_id)
        player = Player(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    birth=data["birth"],
                    civility=data["civility"],
                    rank=data["rank"],
                    id=data.doc_id
                )
        return player

    @classmethod
    def search_by_name(cls):
        '''
        Search a player by name
        '''
        search_result = Database.search('players', PlayersView.search())
        players = cls.create_list(search_result)
        user_choice = PlayersView.list(players)
        player = players[int(user_choice) - 1]
        return player

    @classmethod
    def create_list(cls, results):
        players = []
        results = results
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
        return 'home'
