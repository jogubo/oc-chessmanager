from utils.database import Database
from models.entities.player import Player


class PlayersDAO:

    @staticmethod
    def create_player(serialized_player):
        """
        Create object.

            Parameters:
                serialized_player (dict): Dictionary with data

            Returns:
                player (object): Tournament object created
        """
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
        """
        Get player object.

            Parameters:
                player_id (int): Tournament ID

            Returns:
                player (object): Tournament objects
        """
        player_data = Database.get('players', player_id)
        player_data['id'] = player_data.doc_id
        player = cls.create_player(player_data)
        return player

    @classmethod
    def get_list_players(cls, list_ids='all'):
        """
        Get the list of players objects.

            Parameters:
                list_ids (list, str): Player ID list or
                'all' for  entire list in the database.

            Returns:
                players (list): The list of player objects
        """

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
    def sort_list(cls, players, sort_by='name'):
        """
        Sort a list of players.

            Parameters:
                players (list): list of player objects
                sort_by (str): 'name', 'rank'

            Returns:
                players: sorted list
        """
        if sort_by == 'name':
            players.sort(key=lambda x: x.full_name)
        if sort_by == 'rank':
            players.sort(key=lambda x: int(x.rank))
        return players

    @classmethod
    def search_player_by_name(cls, name_request):
        players_ids = []
        while len(players_ids) < 1:
            players_ids = Database.search('players', name_request)
        players = cls.get_list_players(players_ids)
        return players

    @staticmethod
    def list_formatted_data(
        players,
        force=False
    ):
        """
        Format data for the view.

            Parameters:
                players (object, list): Single object or object list
                force (bool): Set True to force the return of a list

            Returns:
                players_infos (dict, list): The data as a dict or dict list
        """
        single_object = False
        if not isinstance(players, list):
            players = [players]
            single_object = True
        players_infos = []
        for player in players:
            players_infos.append(player.format_data('all'))
        if single_object and not force:
            return players_infos[0]
        else:
            return players_infos
