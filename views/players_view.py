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
    def display_player(cls, player_infos):
        cls.main_display()
        print(player_infos)
        choices = ['M', 'R']
        _input = prompt("[M]odifier le classement | "
                        "[R]etour à la liste des joueurs").upper()
        if _input in choices:
            return _input

    @classmethod
    def list(cls, players, display='all'):
        '''
        players is list :
        players = [{'id': player_id, 'name': player_name}]
        '''
        while True:
            cls.title = "Liste des joueurs\n"
            cls.main_display()
            i, choices = 1, ['A', 'T', 'M', 'Q']
            for player in players:
                print(f"[{i}] - {player['name']} - "
                      f"Rang: {player['rank']}")
                choices.append(i)
                i += 1
            text = "Selectionnez un joueur"
            if display == 'all':
                _input = prompt(f"{text} pour afficher plus d'infos\n"
                                "[A]jouter un joueur | [T]rier | "
                                "[M]enu principal | [Q]uitter le programme")
            elif display == 'minimal':
                _input = prompt(f"{text} :")
            try:
                user_choice = int(_input)
            except ValueError:
                user_choice = _input.upper()
            if user_choice in choices:
                if isinstance(user_choice, int):
                    return players[user_choice - 1]['id']
                else:
                    return user_choice
            else:
                continue

    @classmethod
    def sort_by(cls):
        while True:
            cls.main_display()
            choices = ['N', 'R']
            print("Trier par:\n"
                  "[N]om\n"
                  "[R]ang\n")
            _input = prompt("").upper()
            if _input in choices:
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
    def set_rank(cls, player_name, player_rank=None):
        valid = False
        while not valid:
            cls.main_display()
            print(f"{player_name}")
            print(f"Classement actuel: {player_rank}")
            _input = prompt("Entrez le nouveau classement du joueur:")
            try:
                _input = int(_input)
                if _input > 0:
                    infos = f"{player_name}\n" \
                            f"Rang actuel: {player_rank}\n" \
                            f"Nouveau Rang: {str(_input)}"
                    valid = cls.check(infos, True)
            except ValueError:
                continue
        return _input

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
