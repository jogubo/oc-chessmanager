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

    def serialize(self):
        return {
                "name": self.name,
                "description": self.description,
                "players": self.players
                }
