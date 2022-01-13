from utils. database import Database
from models.entities.player import Player
from models.dao.players_dao import PlayersDAO
from views.players_view import PlayersView


class PlayersCtrl:

    @classmethod
    def get_player(cls, player_id):
        """
        Get a player.

            Parameters:
                player_id (int): tournament id

            Returns:
                next_controller, next_parameters
        """
        player = PlayersDAO.get_player_by_id(player_id)
        user_choice = PlayersView.display_player(player.infos)
        if user_choice == 'M':
            return 'change_player_rank', {'player': player}
        elif user_choice == 'R':
            return 'list_players', {'display': 'all'}

    @classmethod
    def change_player_rank(cls, player):
        player = player
        player_name = player.full_name
        player_rank = player.rank
        new_rank = PlayersView.set_rank(player_name, player_rank)
        Database.update('players', 'rank', new_rank, [player.id])
        return 'get_player', {'player_id': player.id}

    @classmethod
    def list_players(cls, list_players=None, list_ids='all', display=None):
        if list_players is not None:
            players = list_players
        else:
            players = PlayersDAO.get_list_players(list_ids)
        user_choice = PlayersView.list(
            PlayersDAO.list_formatted_data(players),
            display
        )
        if isinstance(user_choice, int):
            return 'get_player', {'player_id': user_choice}
        elif user_choice == 'M':
            return 'home', None
        elif user_choice == 'A':
            return 'new_player', None
        elif user_choice == 'T':
            return 'sort_players', {'players': players}
        elif user_choice == 'Q':
            return 'close_app', None

    @classmethod
    def sort_list_players(cls, players):
        user_choice = PlayersView.sort_by()
        if user_choice == 'N':
            players = PlayersDAO.sort_list(players, sort_by='name')
        if user_choice == 'R':
            players = PlayersDAO.sort_list(players, sort_by='rank')
        return 'list_players', {'list_players': players, 'display': 'all'}

    @classmethod
    def search_by_name(cls):
        '''
        Search a player by name
        '''
        search_request = PlayersView.search()
        players = PlayersDAO.search_player_by_name(search_request)
        user_choice = cls.list_players(list_players=players, display='minimal')
        return user_choice[1]['player_id']

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
        return 'list_players', {'display': 'all'}
