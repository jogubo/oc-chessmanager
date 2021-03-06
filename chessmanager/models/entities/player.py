class Player:
    def __init__(
        self,
        first_name,
        last_name,
        birth,
        civility,
        rank=None,
        id=None
    ):
        self._first_name = first_name
        self._last_name = last_name
        self._birth = birth
        self._civility = civility
        self._rank = rank
        self._id = id
        self._score = 0

    def __repr__(self):
        return f"{self.full_name}"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth

    @property
    def civility(self):
        return self._civility

    @civility.setter
    def civility(self, civility):
        self._civility = civility

    @property
    def rank(self):
        if self._rank is None:
            return ''
        else:
            return self._rank

    @rank.setter
    def rank(self, rank):
        self._rank = rank

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def id(self):
        return self._id

    @property
    def infos(self):
        infos = (
            f"Nom: {self.full_name}\n"
            f"Date de naissance: {self.birth}\n"
            f"Classement: {self.rank}"
        )
        return infos

    def format_data(self, *args):
        """
        Format data for the view.

            Parameters:
                *args (str): 'id', 'name', 'rank', 'score', 'all'

            Returns:
                player_infos (dict)
        """
        player_infos = {}
        if 'id' in args or 'all' in args:
            player_infos['id'] = self.id
        if 'name' in args or 'all' in args:
            player_infos['name'] = self.full_name
        if 'rank' in args or 'all' in args:
            player_infos['rank'] = self.rank
        if 'score' in args or 'all' in args:
            player_infos['score'] = self.score
        return player_infos

    @property
    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth": self.birth,
            "civility": self.civility,
            "rank": self.rank,
        }
