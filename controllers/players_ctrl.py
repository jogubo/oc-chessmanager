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
        user_choice = PlayersView.display_player(player.infos)
        if user_choice == 'change_player_rank':
            return user_choice, {'player': player} 
        else:
            return user_choice

    @classmethod
    def change_player_rank(cls, player):
        player = player
        player_name = player.full_name
        player_rank = player.rank
        new_rank = PlayersView.set_rank(player_name, player_rank)
        Database.update('players', 'rank', new_rank, [player.id])
        return 'list_players', None

    @classmethod
    def search_by_name(cls):
        '''
        Search a player by name
        '''
        players_id = Database.search('players', PlayersView.search())
        #players = cls.create_list(search_result)
        players_infos = []
        for player_infos in player_id:
            pass
        user_choice = PlayersView.list(players)
        player = players[int(user_choice) - 1]
        return player

    @classmethod
    def list_players(cls, list_ids='all', view=None):
        list_ids = list_ids
        players = []
        if list_ids == 'all':
            list_ids = []
            serialized_players = Database.get('players')
            for player in serialized_players:
                list_ids.append(player.doc_id)
        for id in list_ids:
            serialized_player = Database.get('players', id)
            serialized_player['id'] = id
            player = cls.create_player(serialized_player)
            players.append(player)
        players_infos = cls.format_data(players, id=True, name=True)
        user_choice = PlayersView.list(players_infos)
        if isinstance(user_choice, int):
            return 'get_player', {'player_id': user_choice}
        elif user_choice == 'M':
            return 'home', None
        elif user_choice == 'Q':
            return 'close_app', None

    @classmethod
    def format_data(cls, players, id=False, name=False, rank=False):
        players, id, name, rank = players, id, name, rank
        if isinstance(players, int):
            players = [players]
        players_infos = []
        for player in players:
            infos = {}
            if id:
                infos['id'] = player.id
            if name:
                infos['name'] = player.full_name
            if rank:
                infos['rank'] = player.rank
            players_infos.append(infos)
        if len(players) == 1:
            return players_infos[0]
        else:
            return players_infos

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
