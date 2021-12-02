class Match:
    def __init__(self, players, score=None):
        self._players = players
        self._score = score

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players):
        self._players = players

    @property
    def score(self):
        return self._score
