from datetime import date
from utils import constants
from utils import functions


class PlayerFormView:
    def __init__(self, title):
        self.title = title

    def main_display(self):
        functions.clear()
        print(f"[{constants.TITLE}]\n")
        print(f"{self.title}\n")

    def first_name(self):
        self.main_display()
        print("Entrez le prénom du joueur :\n")
        self._first_name = input(">> ").title()

    def last_name(self):
        self.main_display()
        print("Entrez le nom du joueur :\n")
        self._last_name = input(">> ").upper()

    def birth(self):
        while True:
            self.main_display()
            print("Entrez le date de naissance (JJ/MM/AAAA) :\n")
            _input = input('>> ')
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

    def sex(self):
        while True:
            self.main_display()
            print("Entrez le sexe du joueur : [H]omme/[F]emme")
            _input = input('>> ').upper()
            if _input == "H":
                self._sex = "Homme"
                break
            elif _input == "F":
                self._sex = "Femme"
                break
            else:
                continue

    def new(self):
        self._correct = False
        while self._correct is False:
            self.first_name()
            self.last_name()
            self.birth()
            self.sex()
            self.added(True)
        return

    def added(self, validate=False):
        while True:
            validation = validate
            self.main_display()
            if validation is True:
                print(f"{self._first_name} {self._last_name} [{self._sex}] "
                      f"({self._birth})\n\n"
                      "Les informations sont-elles correctes ? : [O]ui/[N]on")
                _input = input('>> ').upper()
                if _input == "O":
                    self._correct = True
                    break
                elif _input == "N":
                    break
                else:
                    continue
