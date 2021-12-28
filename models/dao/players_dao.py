from utils.database import Database
from models.entities.player import Player


class PlayersDAO:

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
    def get_player_by_id(cls, player_id):
        player_data = Database.get('players', player_id)
        player_data['id'] = player_data.doc_id
        player = cls.create_player(player_data)
        return player

    @classmethod
    def get_list_players(cls, list_ids='all'):
        list_ids = list_ids
        players = []
        if list_ids == 'all':
            list_ids = []
            players_data = Database.get('players')
            for player in players_data:
                list_ids.append(player.doc_id)
        for id in list_ids:
            player = cls.get_player_by_id(player_id=id)
            players.append(player)
        return players

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
