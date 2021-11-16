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
        name = prompt("Entrez le nom du tournoi :")
        return name

    def location(self):
        self.main_display()
        location = prompt("Entrez le lieu du tournoi :")
        return location

    def description(self):
        self.main_display()
        description = prompt("Entrez la description du tournoi :")
        return description

    def add_player(self):
        self.main_display()
        _input = prompt("Entrez le nom du joueur recherché :").upper()

    def new(self):
        '''
        Displays a form to create a new tournament
        '''
        tournament = {
                "name": self.name(),
                "description": self.description()
                }
        return tournament
