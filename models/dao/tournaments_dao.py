from utils.database import Database
from models.dao.players_dao import PlayersDAO
from models.entities.tournament import Tournament


class TournamentsDAO:

    @staticmethod
    def create_tournament(serialized_tournament):
        """
        Create object.

            Parameters:
                serialized_tournament (dict): Dictionary with data

            Returns:
                tournament (object): Tournament object created
        """
        tournament = Tournament(
                name=serialized_tournament["name"],
                description=serialized_tournament["description"],
                location="location",
                players_data=serialized_tournament["players_data"],
                date="date",
                turns=serialized_tournament['turns'],
                rounds=serialized_tournament['rounds'],
                time=serialized_tournament['time'],
                id=serialized_tournament['id']
                )
        return tournament

    @classmethod
    def get_tournament_by_id(cls, tournament_id, players=False):
        """
        Get tournament object.

            Parameters:
                tournament_id (int): Tournament ID
                players (bool): Add player objects

            Returns:
                tournament (object): Tournament objects
        """
        tournament_data = Database.get('tournaments', tournament_id)
        tournament_data['id'] = tournament_data.doc_id
        tournament = cls.create_tournament(tournament_data)
        if players:
            tournament.players = cls.get_players_of_the_tournament(tournament)
        return tournament

    @classmethod
    def get_list_tournaments(cls, list_ids='all'):
        """
        Get the list of tournament objects.

            Parameters:
                list_ids (list, str): Tournament ID list or
                'all' for  entire list in the database.

            Returns:
                tournaments (list): The list of tournament objects
        """
        list_ids = list_ids
        tournaments = []
        if list_ids == 'all':
            list_ids = []
            tournaments_data = Database.get('tournaments')
            for tournament in tournaments_data:
                list_ids.append(tournament.doc_id)
        for id in list_ids:
            tournament = cls.get_tournament_by_id(tournament_id=id)
            tournaments.append(tournament)
        return tournaments

    @classmethod
    def get_players_of_the_tournament(cls, tournament, sort=True):
        """
        Get the dict of player objects of a tournament.

            Parameters:
                tournament (object): Single tournament object

            Returns:
                players (dict): Dictionary of player objects
        """
        players = {}
        players_data = tournament.players_data
        for player_id, player_data in players_data.items():
            players[player_id] = PlayersDAO.get_player_by_id(int(player_id))
            players[player_id].score = player_data['score']
            players[player_id].rank = player_data['rank']
        return players

    @classmethod
    def get_rounds_data(cls, tournament):
        players = tournament.players
        rounds_data = {}
        PLAYER_1, PLAYER_2 = 0, 1
        ID, SCORE = 0, 1
        for round in tournament.turns:
            matchs = {}
            i = 1
            for match in round['matchs']:
                matchs[f"Match {i}"] = {
                        'player_1': {
                            'name':
                                players[str(match[PLAYER_1][ID])].full_name,
                            'score':
                                match[PLAYER_1][SCORE]
                            },
                        'player_2': {
                            'name':
                                players[str(match[PLAYER_2][ID])].full_name,
                            'score':
                                match[PLAYER_2][SCORE]
                            }
                        }
                i += 1
            rounds_data[round['name']] = matchs
        return rounds_data

    @staticmethod
    def list_formatted_data(tournaments, force_list=False):
        """
        Format data for the view.

            Parameters:
                tournaments (object, list): Single object or object list
                force_list (bool): Set True to force the return of a list

            Returns:
                tournaments_infos (dict, list): The data as a dict or dict list
        """
        single_object = False
        if not isinstance(tournaments, list):
            tournaments = [tournaments]
            single_object = True
        tournaments_infos = []
        for tournament in tournaments:
            tournaments_infos.append(tournament.format_data('all'))
        if single_object and not force_list:
            return tournaments_infos[0]
        else:
            return tournaments_infos

    @staticmethod
    def update_db(tournament, list_args):
        tournament = tournament
        if 'players_data' in list_args:
            tournament.update_players_data()
            Database.update('tournaments', 'players_data',
                            tournament.players_data, tournament.id)
        if 'turns' in list_args:
            Database.update('tournaments', 'turns',
                            tournament.turns, tournament.id)
        input()

    @staticmethod
    def add_tournaments_in_db(tournaments):
        """
        Add tournaments in the database.

            Parameters:
                tournaments (object, list): Single object or object list
        """
        serialized_tournament = []
        if not isinstance(tournaments, list):
            serialized_tournament.append(tournaments.serialize)
        else:
            for tournament in tournaments:
                serialized_tournament.append(tournament.serialize)
        Database.add('tournaments', serialized_tournament)
