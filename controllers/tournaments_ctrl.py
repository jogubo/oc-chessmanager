from models.dao.tournaments_dao import TournamentsDAO
from models.dao.players_dao import PlayersDAO
from controllers.players_ctrl import PlayersCtrl
from views.tournaments_view import TournamentsView


class TournamentsCtrl:

    @classmethod
    def get_tournament(cls, tournament_id=None, tournament=None):
        finished = False
        if tournament is None:
            tournament = TournamentsDAO.get_tournament_by_id(
                tournament_id=tournament_id,
                players=True
                )
        elif tournament_id is None:
            tournament = tournament
        if tournament.players is not None:
            tournament.players = TournamentsDAO.get_players_of_the_tournament(
                tournament
                )
        if tournament.current_round > tournament.rounds:
            finished = True
        user_choice = TournamentsView.display_tournament(
            tournament.format_data('all'),
            finished
            )
        if user_choice == 'R':
            return 'list_tournaments', {'display': 'all'}
        elif user_choice == 'C':
            return 'tournament_ranking', {'tournament': tournament}
        elif user_choice == 'T':
            return 'list_rounds', {'tournament': tournament}
        elif user_choice == 'P':
            return 'next_round', {'tournament': tournament}

    @classmethod
    def get_ranking(cls, tournament):
        tournament.sort_players()
        TournamentsView.display_ranking(tournament.format_data('all'))
        return 'get_tournament', {'tournament': tournament}

    @classmethod
    def get_next_round(cls, tournament):
        matchs = tournament.generate_versus()
        user_choice = TournamentsView.display_round(
            matchs,
            tournament.format_data('all')
            )
        if user_choice == 'E':
            return 'set_score', {'tournament': tournament}
        elif user_choice == 'R':
            return 'get_tournament', {'tournament': tournament}

    @classmethod
    def list_tournaments(cls, list_ids='all', display=None):
        tournaments = TournamentsDAO.get_list_tournaments(list_ids)
        user_choice = TournamentsView.display_list(
            TournamentsDAO.list_formatted_data(tournaments),
            display='all'
            )
        if isinstance(user_choice, int):
            return 'get_tournament', {'tournament_id': user_choice}
        elif user_choice == 'M':
            return 'home', None
        elif user_choice == 'C':
            return 'new_tournament', None
        elif user_choice == 'Q':
            return 'close_app', None

    def list_matchs(self):
        matchs_list = self._tournament.generate_versus()
        round = self._tournament.current_round
        matchs = []
        for match in matchs_list:
            player_1, player_2 = match
            players = (self._players[player_1], self._players[player_2])
            matchs.append(players)
        TournamentsView.display_matchs_list(round, matchs)

    @classmethod
    def list_rounds(cls, tournament):
        rounds_data = TournamentsDAO.get_rounds_data(tournament)
        TournamentsView.display_rounds(rounds_data)
        return 'get_tournament', {'tournament': tournament}

    @classmethod
    def set_score(cls, tournament):
        PLAYER_1, PLAYER_2 = 0, 1
        matchs = tournament.generate_versus()
        matchs_results = []
        round_name = TournamentsView.set_round_name()
        if round_name is None:
            round_name = f"round_{tournament.current_round}"
        for match in matchs:
            player_1, player_2 = match
            player_1 = tournament.players[player_1]
            player_2 = tournament.players[player_2]
            score = TournamentsView.set_score_match(
                tournament.current_round,
                (player_1.full_name, player_2.full_name)
                )
            player_1.score += score[PLAYER_1]
            players_data = tournament.players_data
            players_data[str(player_1.id)]['history'].append(str(player_2.id))
            player_2.score += score[PLAYER_2]
            players_data[str(player_2.id)]['history'].append(str(player_1.id))
            match = (
                [player_1.id, score[PLAYER_1]],
                [player_2.id, score[PLAYER_2]]
                )
            matchs_results.append(match)
        round = {
            'name': round_name,
            'date': '',
            'matchs': matchs_results
            }
        rounds = tournament.turns
        rounds.append(round)
        tournament.turns = rounds
        TournamentsDAO.update_db(tournament, ('turns', 'players_data'))
        return 'tournament_ranking', {'tournament': tournament}

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
        new_tournament_form['id'] = None
        tournament = TournamentsDAO.create_tournament(new_tournament_form)
        TournamentsDAO.add_tournaments_in_db(tournament)
        return 'home', None
