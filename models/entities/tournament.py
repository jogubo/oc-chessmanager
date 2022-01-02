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
            id=None,
            players=None
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
        self.players = players

    def __repr__(self):
        return f"""
        {self.name}
        {self.description}
        """

    @property
    def infos(self):
        return f"""
        {self.name}
        {self.description}
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
    def players(self):
        return self._players

    @players.setter
    def players(self, players):
        self._players = players

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

        ID, SCORE, RANK = 0, 1, 2
        players.sort(key=lambda x: x[SCORE], reverse=True)
        for i in range(0, len(players)):
            for j in range(0, len(players)-i-1):
                if (players[j][SCORE] == players[j+1][SCORE]):
                    if (players[j][RANK] > players[j+1][RANK]):
                        temp = players[j]
                        players[j] = players[j+1]
                        players[j+1] = temp
        sorted_players = {}
        for player in players:
            sorted_players[player[ID]] = self.players[player[ID]]
        self.players = sorted_players
        return players

    def generate_versus(self):
        players = self.sort_players()
        median = int(len(players) / 2)
        versus = []
        ID, HISTORY = 0, 3
        if len(players[ID][HISTORY]) == 0:
            for i in range(median):
                versus.append((players[i][0], players[i+median][0]))
        else:
            i = 1
            while len(players) > 0:
                try:
                    player_1, player_2 = players[ID], players[i]
                    if player_2[ID] in player_1[HISTORY]:
                        i += 1
                    else:
                        versus.append((player_1[ID], player_2[ID]))
                        del players[i]
                        del players[ID]
                        i = 1
                except IndexError:
                    i = 1
                    versus.append((player_1[ID], player_2[ID]))
                    del players[i]
                    del players[ID]
        return versus

    def update_players_data(self):
        for id, player_data in self.players_data.items():
            player_data['score'] = self.players[id].score

    def format_data(self, *args):
        tournament_infos = {}
        if 'id' in args or 'all' in args:
            tournament_infos['id'] = self.id
        if 'name' in args or 'all' in args:
            tournament_infos['name'] = self.name
        if 'description' in args or 'all' in args:
            tournament_infos['description'] = self.description
        if 'rounds' in args or 'all' in args:
            tournament_infos['total_rounds'] = self.rounds
            tournament_infos['current_round'] = self.current_round
        if 'player' in args or 'all' in args and self.players is not None:
            players_infos = {}
            for id, player in self.players.items():
                players_infos[id] = player.format_data('all')
            tournament_infos['players'] = players_infos
        return tournament_infos

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
