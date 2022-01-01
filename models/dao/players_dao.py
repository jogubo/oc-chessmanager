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
        elif isinstance(list_ids, int):
            list_ids = [list_ids]
        for id in list_ids:
            player = cls.get_player_by_id(player_id=id)
            players.append(player)
        return players

    @classmethod
    def search_player_by_name(cls, name_request):
        players_ids = []
        while len(players_ids) < 1:
            players_ids = Database.search('players', name_request)
        return players_ids

    @staticmethod
    def format_data(
            players,
            id=False,
            name=False,
            rank=False,
            score=False,
            force=False
            ):
        players, id, name, rank = players, id, name, rank
        single_object = False
        if not isinstance(players, list):
            players = [players]
            single_object = True
        players_infos = []
        for player in players:
            infos = {}
            if id:
                infos['id'] = player.id
            if name:
                infos['name'] = player.full_name
            if rank:
                infos['rank'] = player.rank
            if score:
                infos['score'] = player.score
            players_infos.append(infos)
        if single_object and not force:
            return players_infos[0]
        else:
            return players_infos