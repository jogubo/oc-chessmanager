class Tournament:
    def __init__(
            self,
            name,
            description,
            location,
            players_data,
            date,
            turns=[],
            rounds=4,
            time=None,
            id=None
            ):
        self._name = name
        self._location = location
        self._players_data = players_data
        self._date = date
        self._turns = turns
        self._rounds = rounds
        self._time = time
        self._description = description
        self._id = id

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
    def players_data(self):
        return self._players_data

    @players_data.setter
    def players_data(self, players_data):
        self._players_data = players_data

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

    @property
    def current_round(self):
        print(self.rounds)
        return len(self.turns) + 1

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def sort_players(self):
        '''
        Player's data is list:
            [player_id, player_score, player_rank]
        '''
        players_data = self.players_data

        players = []
        for id, data in players_data.items():
            player = [
                    id,
                    data['score'],
                    data['rank'],
                    data['history'],
                    ]
            players.append(player)

        SCORE, RANK = 1, 2
        players.sort(key=lambda x: x[SCORE], reverse=True)
        for i in range(0, len(players)):
            for j in range(0, len(players)-i-1):
                if (players[j][SCORE] == players[j+1][SCORE]):
                    if (players[j][RANK] > players[j+1][RANK]):
                        temp = players[j]
                        players[j] = players[j+1]
                        players[j+1] = temp
        return players

    def generate_versus(self):
        players = self.sort_players()
        median = int(len(players) / 2)
        versus = []
        ID, HISTORY = 0, 3
        if len(players[0][3]) == 0:
            for i in range(median):
                versus.append((players[i][0], players[i+median][0]))
        else:
            i = 1
            while len(players) > 0:
                player_1, player_2 = players[ID], players[i]
                if player_2[ID] in player_1[HISTORY]:
                    i += 1
                else:
                    versus.append((player_1[ID], player_2[ID]))
                    del players[i]
                    del players[ID]
                    i = 1
        return versus

    @property
    def serialize(self):
        return {
                'name': self.name,
                'description': self.description,
                'date': self.date,
                'location': self.location,
                'players_data': self.players_data,
                'turns': self.turns,
                'rounds': self.rounds,
                'time': self.time
                }
