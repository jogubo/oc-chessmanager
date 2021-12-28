from utils.database import Database
from models.dao.tournaments_dao import TournamentsDAO
from models.entities.tournament import Tournament
from models.dao.players_dao import PlayersDAO
from controllers.players_ctrl import PlayersCtrl
from views.tournaments_view import TournamentsView
from views.players_view import PlayersView


class TournamentsCtrl:
    def __init__(self, tournament_id):
        tournament = TournamentsDAO.get_tournament_by_id(tournament_id)
        players = TournamentsDAO.get_players_of_the_tournament(tournament)
        self.tournament, self.players = tournament, players

    @classmethod
    def list_tournaments(cls, list_ids='all', display=False):
        list_ids = list_ids
        tournaments = []
        if list_ids == 'all':
            list_ids = []
            serialized_tournaments = Database.get('tournaments')
            for tournament in serialized_tournaments:
                list_ids.append(tournament.doc_id)
        for id in list_ids:
            serialized_tournament = Database.get('tournament', id)
            serialized_tournament['id'] = serialized_tournament.doc_id
            tournament = TournamentsCtrl(serialized_tournament.doc_id)
            tournaments.append(tournament)
        if not display:
            return tournaments
        tournaments_infos = cls.format_data(tournaments, id=True, name=True)
        user_choice = PlayersView.list(tournaments_infos, display)
        if isinstance(user_choice, int):
            return 'get_tournament', {
                    'tournament_id': user_choice,
                    'players': False
                    }
        elif user_choice == 'M':
            return 'home', None
        elif user_choice == 'A':
            return 'new_tournament', None
        elif user_choice == 'Q':
            return 'close_app', None

    def resume_match(self):
        while self._tournament.current_round <= self._tournament.rounds:
            self.set_score()

    def list_matchs(self):
        matchs_list = self._tournament.generate_versus()
        round = self._tournament.current_round
        matchs = []
        for match in matchs_list:
            player_1, player_2 = match
            players = (self._players[player_1], self._players[player_2])
            matchs.append(players)
        TournamentsView.display_matchs_list(round, matchs)

    def set_score(self):
        PLAYER_1, PLAYER_2 = 0, 1
        matchs = self._tournament.generate_versus()
        matchs_results = []
        for match in matchs:
            player_1, player_2 = match
            player_1 = self._players[player_1]
            player_2 = self._players[player_2]
            players = (player_1.full_name, player_2.full_name)
            score = TournamentsView.set_score_match(
                    self._tournament.current_round,
                    players
                    )
            player_1.score += score[PLAYER_1]
            player_2.score += score[PLAYER_2]
            match = (
                    [player_1.id, score[PLAYER_1]],
                    [player_2.id, score[PLAYER_2]]
                    )
            matchs_results.append(match)
        round = {
                'name': 'Hello World',
                'date': '12/12/2012',
                'matchs': matchs_results
                }
        print(self._tournament.turns)
        rounds = self._tournament.turns
        rounds.append(round)
        self._tournament.turns = rounds
        Database.update('tournaments', 'turns', rounds, [5])

    @staticmethod
    def create_new():
        new_tournament_form = TournamentsView.create_new_tournament()
        players = {}
        total_players = new_tournament_form["nb_players"]
        while total_players > 0:
            search_player = PlayersCtrl.search_by_name()
            player = PlayersDAO.get_player_by_id(search_player)
            if player.id not in players:
                players[player.id] = {
                        'score': 0.0,
                        'rank': player.rank,
                        'history': []
                        }
                total_players -= 1
        new_tournament_form['players'] = players
        new_tournament_form['turns'] = []
        new_tournament_form['rounds'] = 4
        new_tournament_form['time'] = 'Blitz'
        tournament = TournamentsDAO.create_tournament(new_tournament_form)
        TournamentsDAO.add_tournament_in_db(tournament)
        return 'home'
