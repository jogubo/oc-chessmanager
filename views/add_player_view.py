import datetime


class AddPlayerView:
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._birth = None

    def first_name(self):
        print("Entrez le prénom du joueur :\n")
        self._first_name = input(">> ").capitalize()

    def last_name(self):
        print("Entrez le nom du joueur :\n")
        self._last_name = input(">> ").upper()

    def birth(self):
        while True:
            print("Entrez le date de naissance (AAAA-MM-JJ) :\n")
            _input = input('>> ')
            try:
                _input = _input.split('-')
                year = int(_input[0])
                month = int(_input[1])
                day = int(_input[2])
                self._birth = datetime.date(year, month, day)
                break
            except ValueError:
                continue
            except IndexError:
                continue

    @property
    def added(self):
        print(f"{self._first_name} {self._last_name} ({(self._birth)})"
              " a été ajouté avec succès.")
