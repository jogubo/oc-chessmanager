from datetime import date
from utils import constants
from utils import functions


class AddPlayerView:
    def __init__(self, title):
        self.title = title
        self._first_name = None
        self._last_name = None
        self._birth = None

    def first_name(self):
        functions.clear()
        print(f"[{constants.TITLE}]\n")
        print(f"{self.title}\n")
        print("Entrez le prénom du joueur :\n")
        self._first_name = input(">> ").capitalize()

    def last_name(self):
        functions.clear()
        print(f"[{constants.TITLE}]\n")
        print(f"{self.title}\n")
        print("Entrez le nom du joueur :\n")
        self._last_name = input(">> ").upper()

    def birth(self):
        functions.clear()
        while True:
            print(f"[{constants.TITLE}]\n")
            print(f"{self.title}\n")
            print("Entrez le date de naissance (AAAA-MM-JJ) :\n")
            _input = input('>> ')
            try:
                _input = _input.split('-')
                year = int(_input[0])
                month = int(_input[1])
                day = int(_input[2])
                self._birth = date(year, month, day)
                break
            except ValueError:
                continue
            except IndexError:
                continue

    def new(self):
        self._correct = False
        while self._correct is False:
            self.first_name()
            self.last_name()
            self.birth()
            self.added(True)
        return

    def added(self, validate=False):
        while True:
            validation = validate
            functions.clear()
            print(f"[{constants.TITLE}]\n")
            print(f"{self.title}\n")
            if validation is True:
                print(f"{self._first_name} {self._last_name} ({(self._birth)})"
                      "\nLes informations sont-elles correctes ? (O/N) :")
                _input = input('>> ').upper()
                if _input == "O":
                    self._correct = True
                    break
                elif _input == "N":
                    break
                else:
                    continue
