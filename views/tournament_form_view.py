# from datetime import date
from utils import constants
from utils import functions


class TournamentFormView:
    def __init__(self, title):
        self.title = title

    def main_display(self):
        functions.clear()
        print(f"[{constants.TITLE}]\n")
        print(f"{self.title}\n")

    def name(self):
        self.main_display()
        print("Entrez le nom du tournoi :")
        self._name = input('>> ')

    def place(self):
        self.main_display()
        print("Entrez le lieu du tournoi :")
        self._place = input('>> ')

    def description(self):
        self.main_display()
        print("Entrez la description du tournoi :")
        self._description = input('>> ')
