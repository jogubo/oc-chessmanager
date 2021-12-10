from utils.database import Database
from models.tournament import Tournament
from controllers.players_ctrl import PlayersCtrl
from views.tournaments_view import TournamentsView


class TournamentsCtrl:
    def __init__(self, tournament_id):
        data = Database.get('tournaments', tournament_id)
        self._tournament = Tournament(
                data["name"],
                data["description"],
                "location",
                data["players_data"],
                "date",
                "turns",
                "rounds",
                "time",
                {}
                )
        self._players = {}
        for player_id, player_data in self._tournament.players_data.items():
            self._players[player_id] = PlayersCtrl.get_player(int(player_id))
            self._players[player_id].score = player_data['score']
            self._players[player_id].rank = player_data['rank']

    def list_matchs(self):
        matchs_list = self._tournament.generate_versus()
        matchs = []
        for match in matchs_list:
            player_1, player_2 = match
            players = (self._players[player_1], self._players[player_2])
            matchs.append(players)
        TournamentsView.display_matchs_list(matchs)

    def set_score(self):
        matchs = self._tournament.generate_versus()
        for match in matchs:
            player_1, player_2 = match
            players = [
                    self._players[player_1],
                    self._players[player_2]
                    ]
            match = TournamentsView.set_score_match(4, players)

        print(self._players['6'].score)

    @staticmethod
    def create_new():
        form = TournamentsView.create_new_tournament()
        players, ids = {}, []
        total_players = form["nb_players"]
        while total_players > 0:
            player = PlayersCtrl.search_by_name()
            print(player.id)
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
                "turns",
                "rounds",
                "Blitz",
                )
        serialized_tournaments = []
        serialized_tournaments.append(tournament.serialize())
        Database.add('tournaments', serialized_tournaments)
        return 'home'
