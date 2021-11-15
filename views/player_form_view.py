from datetime import date
from utils.constants import APP_NAME
from utils.functions import clear, prompt


class PlayerFormView:
    def __init__(self, menu_title):
        self.menu_title = menu_title

    def main_display(self):
        clear()
        print(f"[{APP_NAME}]\n")
        print(f"{self.title}\n")

    def first_name(self):
        self.main_display()
        first_name = prompt("Entrez le prénom du joueur :").title()
        return first_name

    def last_name(self):
        self.main_display()
        last_name = prompt("Entrez le nom du joueur :").upper()
        return last_name

    def birth(self):
        while True:
            self.main_display()
            _input = prompt("Entrez le date de naissance (JJ/MM/AAAA) :")
            try:
                _input = _input.split('/')
                year = int(_input[2])
                month = int(_input[1])
                day = int(_input[0])
                birth = date(year, month, day)
                break
            except ValueError:
                continue
            except IndexError:
                continue
        return birth

    def civility(self):
        while True:
            self.main_display()
            _input = prompt("Entrez le sexe du joueur : [H]omme/[F]emme")
            _input = _input.upper()
            if _input == "H":
                civility = "Homme"
                break
            elif _input == "F":
                civility = "Femme"
                break
            else:
                continue
        return civility

    def new(self):
        valid_form = False
        while valid_form is False:
            player = {
                    "first_name": self.first_name(),
                    "last_name": self.last_name(),
                    "birth": str(self.birth()),
                    "civility": self.civility()
                    }
            infos = f"{player['first_name']} {player['last_name']} " \
                    f"[{player['civility']}] ({player['birth']})\n"

            valid_form = self.check(infos, True)
        return player

    def check(self, infos, validation=False):
        while True:
            validation = validation
            self.main_display()
            if validation is True:
                print(infos)
                _input = prompt("Les informations sont-elles correctes ? : "
                                "[O]ui/[N]on").upper()
                if _input == "O":
                    return True
                elif _input == "N":
                    return False
                else:
                    continue
