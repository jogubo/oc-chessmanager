from tinydb import TinyDB


class Player:
    def __init__(self, first_name, last_name, birth, civility):
        self._first_name = first_name
        self._last_name = last_name
        self._birth = birth
        self._civility = civility
        self._rank = None

    def __repr__(self):
        return f"{self.last_name} {self.first_name}"

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

    def serialize(self):
        self._serialized_player = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "birth": self.birth,
                "civility": self.civility,
                "rank": self.rank
                }
