class Match:
    def __init__(self, players):
        self.player_1, self.player_2 = players

    @property
    def serialize(self):
        player_1, player_2 = self.player_1, self.player_2
        serialized_match = {
                'player_1': {
                    'id': player_1.id,
                    'score': player_1.score
                    },
                'player_2': {
                    'id': player_2.id,
                    'score': player_2.score
                    }
                }
        return serialized_match
