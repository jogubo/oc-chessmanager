from utils.database import Database
from models.dao.tournaments_dao import TournamentsDAO
from models.dao.players_dao import PlayersDAO
from controllers.players_ctrl import PlayersCtrl
from views.tournaments_view import TournamentsView


class TournamentsCtrl:

    @classmethod
    def get_tournament(cls, tournament_id):
        tournament = TournamentsDAO.get_tournament_by_id(
                tournament_id=tournament_id,
                players=True
                )
        tournament_infos = TournamentsDAO.format_data(
                tournaments=tournament,
                name=True,
                description=True,
                players=True
                )
        user_choice = TournamentsView.display_tournament(tournament_infos)
        if user_choice == 'R':
            return 'list_tournaments', {'display': 'all'}

    @classmethod
    def list_tournaments(cls, list_ids='all', display=None):
        tournaments = TournamentsDAO.get_list_tournaments(list_ids)
        tournaments_infos = TournamentsDAO.format_data(
                tournaments=tournaments,
                id=True,
                name=True,
                force=True
                )
        user_choice = TournamentsView.display_list(tournaments_infos, display='all')
        if isinstance(user_choice, int):
            return 'get_tournament', {'tournament_id': user_choice}
        elif user_choice == 'M':
            return 'home', None
        elif user_choice == 'C':
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
        players_data = {}
        total_players = new_tournament_form["nb_players"]
        while total_players > 0:
            search_player = PlayersCtrl.search_by_name()
            player = PlayersDAO.get_player_by_id(search_player)
            if player.id not in players_data:
                players_data[player.id] = {
                        'score': 0.0,
                        'rank': player.rank,
                        'history': []
                        }
                total_players -= 1
        new_tournament_form['players_data'] = players_data
        new_tournament_form['turns'] = []
        new_tournament_form['rounds'] = 4
        new_tournament_form['time'] = 'Blitz'
        new_tournament_form['id'] = None
        tournament = TournamentsDAO.create_tournament(new_tournament_form)
        TournamentsDAO.add_tournaments_in_db(tournament)
        return 'home', None
