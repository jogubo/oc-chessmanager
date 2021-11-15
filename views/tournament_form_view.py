# from datetime import date
from utils import constants
from utils import functions


class TournamentFormView:
    '''
    This class contains the view for displaying a tournament creation
    or modification form
    '''

    def __init__(self, menu_title):
        self.menu_title = menu_title

    def main_display(self):
        functions.clear()
        print(f"[{constants.APP_NAME}]\n")
        print(f"{self.menu_title}\n")

    def name(self):
        self.main_display()
        print("Entrez le nom du tournoi :")
        name = input('>> ')
        return name

    def location(self):
        self.main_display()
        print("Entrez le lieu du tournoi :")
        location = input('>> ')
        return location

    def description(self):
        self.main_display()
        print("Entrez la description du tournoi :")
        description = input('>> ')
        return description

    def new(self):
        '''
        Displays a form to create a new tournament
        '''
        tournament = {
                "name": self.name(),
                "description": self.description()
                }
        return tournament
