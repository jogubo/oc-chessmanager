from datetime import date
from utils.constants import TITLE
from utils.functions import clear, prompt


class PlayerFormView:
    def __init__(self, title):
        self.title = title

    def main_display(self):
        clear()
        print(f"[{TITLE}]\n")
        print(f"{self.title}\n")

    def first_name(self):
        self.main_display()
        self._first_name = prompt("Entrez le prénom du joueur :").title()
        return self._first_name

    def last_name(self):
        self.main_display()
        self._last_name = prompt("Entrez le nom du joueur :").upper()
        return self._last_name

    def birth(self):
        while True:
            self.main_display()
            _input = prompt("Entrez le date de naissance (JJ/MM/AAAA) :")
            try:
                _input = _input.split('/')
                year = int(_input[2])
                month = int(_input[1])
                day = int(_input[0])
                self._birth = date(year, month, day)
                break
            except ValueError:
                continue
            except IndexError:
                continue
        return self._birth

    def civility(self):
        while True:
            self.main_display()
            _input = prompt("Entrez le sexe du joueur : [H]omme/[F]emme")
            _input = _input.upper()
            if _input == "H":
                self._civility = "Homme"
                break
            elif _input == "F":
                self._civility = "Femme"
                break
            else:
                continue
        return self._civility

    def new(self):
        self._correct = False
        while self._correct is False:
            self._form = {
                    "first_name": self.first_name(),
                    "last_name": self.last_name(),
                    "birth": str(self.birth()),
                    "civility": self.civility()
                    }
            self.added(True)
        return self._form

    def added(self, validate=False):
        while True:
            validation = validate
            self.main_display()
            if validation is True:
                print(f"{self._first_name} {self._last_name} "
                      f"[{self._civility}] ({self._birth})\n")
                _input = prompt("Les informations sont-elles correctes ? : "
                                "[O]ui/[N]on").upper()
                if _input == "O":
                    self._correct = True
                    break
                elif _input == "N":
                    break
                else:
                    continue
