from utils.database import Database
from models.dao.players_dao import PlayersDAO
from models.entities.tournament import Tournament


class TournamentsDAO:

    @staticmethod
    def create_tournament(serialized_tournament):
        tournament = Tournament(
                name=serialized_tournament["name"],
                description=serialized_tournament["description"],
                location="location",
                players=serialized_tournament["players_data"],
                date="date",
                turns=serialized_tournament['turns'],
                rounds=serialized_tournament['rounds'],
                time="time",
                id=serialized_tournament['id']
                )
        return tournament

    @classmethod
    def get_tournament_by_id(cls, tournament_id):
        tournament_data = Database.get('tournaments', tournament_id)
        tournament_data['id'] = tournament_data.doc_id
        tournament = cls.create_tournament(tournament_data)
        return tournament

    @classmethod
    def get_list_tournaments(cls, list_ids='all'):
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
    def get_players_of_the_tournament(cls, tournament):
        players = {}
        players_data = tournament.players_data()
        for player_id, player_data in players_data.items():
            players[player_id] = PlayersDAO.get_player_by_id(int(player_id))
            players[player_id].score = player_data['score']
            players[player_id].rank = player_data['rank']
        return players

    @staticmethod
    def format_data(tournaments, id=False, name=False):
        tournaments, id, name = tournaments, id, name
        if isinstance(tournaments, int):
            tournaments = [tournaments]
        tournaments_infos = []
        for tournament in tournaments:
            infos = {}
            if id:
                infos['id'] = tournament.id
            if name:
                infos['name'] = tournament.full_name
            tournaments_infos.append(infos)
        if len(tournaments) == 1:
            return tournaments_infos[0]
        else:
            return tournaments_infos

    @staticmethod
    def add_tournament_in_db(tournament):
        Database.add('tournaments', [tournament.serialize])
