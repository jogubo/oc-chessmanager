from utils.database import Database
from models.tournament import Tournament
from controllers.players_ctrl import PlayersCtrl
from views.tournaments_view import TournamentsView
from views.players_view import PlayersView


class TournamentsCtrl:
    def __init__(self, tournament_id):
        data = Database.get('tournaments', tournament_id)
        self._tournament = Tournament(
                data["name"],
                data["description"],
                "location",
                data["players_data"],
                "date",
                data['turns'],
                data['rounds'],
                "time",
                )
        self._players = {}
        for player_id, player_data in self._tournament.players_data.items():
            self._players[player_id] = PlayersCtrl.get_player(int(player_id))
            self._players[player_id].score = player_data['score']
            self._players[player_id].rank = player_data['rank']

    def resume_match(self):
        current_round = self._tournament.current_round
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
            score = TournamentsView.set_score_match(self._tournament.current_round, players)
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
        form = TournamentsView.create_new_tournament()
        players, ids = {}, []
        total_players = form["nb_players"]
        while total_players > 0:
            player = PlayersCtrl.search_by_name()
            if player.id in ids:
                continue
            players[player.id] = {
                    'score': 0.0,
                    'rank': player.rank,
                    'history': []
                    }
            ids.append(player.id)
            total_players -= 1
        tournament = Tournament(
                form["name"],
                form["description"],
                form["location"],
                players,
                form["date"],
                [],
                4,
                "Blitz",
                )
        serialized_tournaments = []
        serialized_tournaments.append(tournament.serialize())
        Database.add('tournaments', serialized_tournaments)
        return 'home'
