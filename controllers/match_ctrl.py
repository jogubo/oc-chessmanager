from controllers.players_ctrl import PlayersCtrl
from models.match import Match
from utils.database import Database


class MatchCtrl:

    @classmethod
    def create_new(cls, players_id):
        players = []
        for id in players_id:
            player = PlayersCtrl.get_player(id)
            player.score = 0.0
            players.append(player)
        match = Match(players)
        serialized_match = []
        serialized_match.append(match.serialize)
        Database.add('match', serialized_match)
