from utils. database import Database
from models.player import Player
from views.players_view import PlayersView


class PlayersCtrl:

    @classmethod
    def get_list(cls) -> None:
        serialized_players = Database.get('players')
        for player in serialized_players:
            player["id"] = player.doc_id
        players = cls.create_list(serialized_players)
        print(serialized_players)
        PlayersView.list(players)
        return 'home'

    @staticmethod
    def get_player(id):
        player_data = Database.get('players', id)
        return Player(
                    first_name=player_data["first_name"],
                    last_name=player_data["last_name"],
                    birth=player_data["birth"],
                    civility=player_data["civility"],
                    rank=player_data["rank"],
                    id=player_data.doc_id
                )

    @classmethod
    def search_by_name(cls):
        '''
        Search a player by name
        '''
        search_result = Database.search('players', PlayersView.search())
        players = cls.create_list(search_result)
        user_choice = PlayersView.list(players)
        player = players[int(user_choice) - 1]
        return player.serialize

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
