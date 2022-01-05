class Match:
    def __init__(self, players):
        self.player_1, self.player_2 = players

    @property
    def serialize(self):
        player_1, player_2 = self.player_1, self.player_2
        ID, SCORE = 0, 1
        serialized_match = {
            'player_1': {
                'id': player_1[ID],
                'score': player_1[SCORE]
                },
            'player_2': {
                'id': player_2[ID],
                'score': player_2[SCORE]
                }
            }
        return serialized_match
