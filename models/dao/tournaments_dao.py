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
                time="time",
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

    @staticmethod
    def format_data(
            tournaments,
            id=False,
            name=False,
            description=False,
            players=False,
            force=False
            ):
        """
        Format data for the view.

            Parameters:
                tournaments (object, list): Single object or object list
                id (bool): Add ID in the data
                name (bool): Add name in the data
                force (bool): Set True to force the return of a list

            Returns:
                tournaments_infos (dict, list): The data as a dict or dict list
        """
        list_tournaments, id, name = tournaments, id, name
        single_object = False
        if not isinstance(list_tournaments, list):
            tournaments = [tournaments]
            single_object = True
        tournaments_infos = []
        for tournament in tournaments:
            infos = {}
            if id:
                infos['id'] = tournament.id
            if name:
                infos['name'] = tournament.name
            if description:
                infos['description'] = tournament.description
            if players and tournament.players is not None:
                players = tournament.players
                players_infos = {}
                for id, player in players.items():
                    players_infos[id] = PlayersDAO.format_data(
                            players=player,
                            name=True,
                            score=True,
                            rank=True
                            )
                infos['players'] = players_infos
            tournaments_infos.append(infos)
        if single_object and not force:
            return tournaments_infos[0]
        else:
            return tournaments_infos

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
