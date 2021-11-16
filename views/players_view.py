from utils.constants import APP_NAME
from utils.functions import clear, prompt


class PlayersView:
    def __init__(self, title):
        self.title = title

    def main_display(self):
        clear()
        print(f"[{APP_NAME}]\n")
        print(f"{self.title}\n")

    def list(self, players):
        self.main_display()
        i = 1
        for player in players:
            print(f"[{i}] - {player}")
            i += 1
        _input = prompt('')
        return _input

    def search(self):
        self.main_display()
        _input = prompt("Entrez le nom du joueur recherché :").upper()
        return _input
