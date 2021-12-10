from datetime import date
from utils.constants import APP_NAME, NUMBER_PLAYERS
from utils.functions import clear, prompt


class TournamentsView:

    @classmethod
    def main_display(cls):
        clear()
        print(f"[{APP_NAME}]\n")
        print(f"{cls.title}\n")

    @classmethod
    def set_name(cls):
        cls.main_display()
        name = prompt("Entrez le nom du tournoi :").title()
        return name

    @classmethod
    def set_location(cls):
        cls.main_display()
        location = prompt("Entrez le lieu du tournoi :").upper()
        return location

    @classmethod
    def set_description(cls):
        cls.main_display()
        description = prompt("Entrez la description du tournoi :").capitalize()
        return description

    @classmethod
    def set_date(cls):
        valid_date = False
        while not valid_date:
            cls.main_display()
            _input = prompt("Entrez le date de l'évènement (JJ/MM/AAAA) :")
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
    def set_nb_players(cls):
        return NUMBER_PLAYERS

    @classmethod
    def add_player(cls):
        cls.main_display()
        _input = prompt("Entrez le nom du joueur recherché :").upper()
        return _input

    @classmethod
    def display_matchs_list(cls, matchs):
        for players in matchs:
            player_1, player_2 = players
            print(f"{player_1.full_name}  vs {player_2.full_name}\n")

    @classmethod
    def set_score_match(cls, round, players):
        while True:
            cls.title = f"Tour {round}:\n"
            cls.main_display()
            player_1, player_2 = players
            print(f"[1] - {player_1}")
            print(f"[2] - {player_2}")
            print("[E] - Égalité")
            _input = prompt("Selectionnez le joueur gagnant").upper()
            if _input == "1":
                player_1.score += 1.0
                return ([player_1.id, 1.0], [player_2.id, 0.0])
            elif _input == "2":
                player_2.score += 1.0
                return ([player_1.id, 0.0], [player_2.id, 1.0])
            elif _input == "E":
                player_1.score += 0.5
                player_2.score += 0.5
                return ([player_1.id, 0.5], [player_2.id, 0.5])

    @classmethod
    def create_new_tournament(cls):
        '''
        Displays a form to create a new tournament
        '''
        cls.title = "Création d'un nouveau tournoi"
        tournament = {
                "name": cls.set_name(),
                "description": cls.set_description(),
                "date": cls.set_date(),
                "location": cls.set_location(),
                "nb_players": cls.set_nb_players(),
                }
        return tournament
