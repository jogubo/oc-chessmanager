from datetime import date
from utils.constants import APP_NAME
from utils.functions import clear, prompt


class PlayersView:

    title = ''

    @classmethod
    def main_display(cls):
        clear()
        print(f"[{APP_NAME}]\n")
        print(f"{cls.title}")

    @classmethod
    def list(cls, players):
        cls.title = "Liste des joueurs\n"
        cls.main_display()
        i = 1
        for player in players:
            print(f"[{i}] - {player}")
            i += 1
        _input = prompt('')
        return _input

    @classmethod
    def search(cls):
        cls.main_display()
        _input = prompt("Entrez le nom du joueur recherché :").upper()
        return _input

    @classmethod
    def set_first_name(cls):
        cls.main_display()
        first_name = prompt("Entrez le prénom du joueur :").title()
        return first_name

    @classmethod
    def set_last_name(cls):
        cls.main_display()
        last_name = prompt("Entrez le nom du joueur :").upper()
        return last_name

    @classmethod
    def set_birth(cls):
        valid_date = False
        while not valid_date:
            cls.main_display()
            _input = prompt("Entrez le date de naissance (JJ/MM/AAAA) :")
            try:
                _input = _input.split('/')
                year = int(_input[2])
                month = int(_input[1])
                day = int(_input[0])
                birth = str(date(year, month, day))
                break
            except ValueError:
                continue
            except IndexError:
                continue
        return birth

    @classmethod
    def set_civility(cls):
        while True:
            cls.main_display()
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

    @classmethod
    def create_new_player(cls):
        '''
        Displays a form to create a new player

            Returns:
                Dictionary (dict)
        '''
        cls.title = "Ajouter un nouveau joueur"
        valid_form = False
        while valid_form is False:
            player = {
                    "first_name": cls.set_first_name(),
                    "last_name": cls.set_last_name(),
                    "birth": cls.set_birth(),
                    "civility": cls.set_civility()
                    }
            infos = f"{player['first_name']} {player['last_name']} " \
                    f"[{player['civility']}] ({player['birth']})\n"

            valid_form = cls.check(infos, True)
        return player

    @classmethod
    def check(cls, infos, validation=False):
        '''
        Displays the values entered in the form and confirmation request

            Parameters:
                infos (str): The modified informations to be desplayed
                validation (bool):  Display a confirmation request

                Returns:
                    Boolean (bool): Return True if the form is correct
        '''
        while True:
            validation = validation
            cls.main_display()
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
