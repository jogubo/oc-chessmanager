# from datetime import date
from utils import constants
from utils.functions import clear, prompt


class TournamentFormView:
    '''
    This class contains the view for displaying a tournament creation
    or modification form
    '''

    def __init__(self, menu_title):
        self.menu_title = menu_title

    def main_display(self):
        clear()
        print(f"[{constants.APP_NAME}]\n")
        print(f"{self.menu_title}\n")

    def name(self):
        self.main_display()
        name = prompt("Entrez le nom du tournoi :").title()
        return name

    def location(self):
        self.main_display()
        location = prompt("Entrez le lieu du tournoi :").upper()
        return location

    def description(self):
        self.main_display()
        description = prompt("Entrez la description du tournoi :").capitalize()
        return description

    def nb_players(self):
        # while True:
        #    self.main_display()
        #    number = prompt("Indiquez le nombre de joueurs pour ce tournoi")
        #    try:
        #        number = int(number)
        #        if number >= 4 and (number % 4) == 0:
        #            return number
        #        else:
        #            continue
        #    except ValueError:
        #        continue
        return constants.NUMBER_PLAYERS

    def add_player(self):
        self.main_display()
        _input = prompt("Entrez le nom du joueur recherché :").upper()

    def new(self):
        '''
        Displays a form to create a new tournament
        '''
        tournament = {
                "name": self.name(),
                "description": self.description(),
                "location": self.location(),
                "nb_players": self.nb_players()
                }
        return tournament
