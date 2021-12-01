class Tournament:
    def __init__(
            self,
            name,
            location,
            players,
            date,
            turns,
            rounds,
            time,
            description
            ):
        self._name = name
        self._location = location
        self._players = players
        self._date = date
        self._turns = turns
        self._rounds = rounds
        self._time = time
        self._description = description

    def __repr__(self):
        return f"""
        {self.name}
        {self.description}
        Joueurs participants:
        {self.players}
        """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def players(self):
        players_id = self._players
        return players_id

    @players.setter
    def players(self, players_id):
        self._players = players_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def turns(self):
        return self._turns

    @turns.setter
    def turns(self, nb):
        self._turns = nb

    @property
    def rounds(self):
        return self._rounds

    @rounds.setter
    def rounds(self, nb):
        self._rounds = nb

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, text):
        self._description = text

    def sort_players(self):
        '''
        Player's data is list:
            [player_id, player_score, player_rank]
        '''
        players = self.players
        score, rank = 1, 2
        players.sort(key=lambda x: x[score], reverse=True)
        for i in range(0, len(players)):
            for j in range(0, len(players)-i-1):
                if (players[j][score] == players[j+1][score]):
                    if (players[j][rank] > players[j+1][rank]):
                        temp = players[j]
                        players[j] = players[j+1]
                        players[j+1] = temp
        self.players = players
        return players

    def generate_versus(self):
        players = self.players
        median = int(len(players) / 2)
        versus = []
        if len(players[0]) == 3:
            for i in range(median):
                versus.append((players[i][0], players[i+median][0]))
        else:
            while len(versus) < median:
                i, j = 0, 1
                while len(players) > 0:
                    history = players[i][3]
                    player = players[j][0]
                    if player in history:
                        j = j+1
                    else:
                        versus.append((players[i][0], players[j][0]))
                        del players[j]
                        del players[i]
        return versus

    def serialize(self):
        return {
                "name": self.name,
                "description": self.description,
                "players": self.players
                }
