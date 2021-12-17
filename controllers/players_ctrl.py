from utils. database import Database
from models.player import Player
from views.players_view import PlayersView


class PlayersCtrl:

    @staticmethod
    def create_player(serialized_player):
        player = Player(
                    first_name=serialized_player["first_name"],
                    last_name=serialized_player["last_name"],
                    birth=serialized_player["birth"],
                    civility=serialized_player["civility"],
                    rank=serialized_player["rank"],
                    id=serialized_player['id']
                )
        return player

    @classmethod
    def get_player(cls, player_id):
        player_data = Database.get('players', player_id)
        player_data['id'] = player_data.doc_id
        player = cls.create_player(player_data)

    @classmethod
    def get_list_players(cls, list_ids=None):
        if list_ids is None:
            players_data = Database.get('players')
        players = []
        for player_data in players_data:
            player = {}
            player_data['id'] = player_data.doc_id
            player = cls.create_player(player_data)
            players.append(player)
        # View
        players_infos = []
        for player in players:
            players_infos.append(player.full_name)
        user_choice = players[PlayersView.list(players_infos)]
        print(user_choice)
        return 'home'

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
            player = Database.get(player.doc_id)
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
