from datetime import date
from utils import constants
from utils.functions import clear, prompt


class PlayerFormView:
    def __init__(self, title):
        self.title = title

    def main_display(self):
        clear()
        print(f"[{constants.TITLE}]\n")
        print(f"{self.title}\n")

    def first_name(self):
        self.main_display()
        self._first_name = prompt("Entrez le prénom du joueur :").title()

    def last_name(self):
        self.main_display()
        self._last_name = prompt("Entrez le nom du joueur :").upper()

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

    def new(self):
        self._correct = False
        while self._correct is False:
            self.first_name()
            self.last_name()
            self.birth()
            self.civility()
            self.added(True)
        return

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
