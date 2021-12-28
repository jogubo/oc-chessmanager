from utils.database import Database
from models.entities.tournament import Tournament
from controllers.players_ctrl import PlayersCtrl
from views.tournaments_view import TournamentsView
from views.players_view import PlayersView


class TournamentsCtrl:
    def __init__(self, tournament_id, players=True):
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
                id=tournament_id
                )
        if players:
            self._players = {}
            players_data = self._tournament.players_data.items()
            for player_id, player_data in players_data.items():
                self._players[player_id] = PlayersCtrl.get_player(
                        int(player_id)
                        )
                self._players[player_id].score = player_data['score']
                self._players[player_id].rank = player_data['rank']

    @classmethod
    def create_tournament(cls, serialized_tournament):
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
    def get_tournament(cls, tournament_id, players=True):
        tournament_data = Database.get('tournaments', tournament_id)
        tournament_data['id'] = tournament_data.doc_id
        tournament = cls.create_tournament(tournament_data)
        if players:
            players = {}
            for player_id, player_data in tournament.players_data.items():
                players[player_id] = PlayersCtrl.get_player(
                        int(player_id)
                        )
                players[player_id].score = player_data['score']
                players[player_id].rank = player_data['rank']
            return 'tournament', {'tournament': tournament, 'players': players}
        return 'tournament', {'tournament': tournament}

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

    @classmethod
    def format_data(cls, tournaments, id=False, name=False):
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
