from utils.constants import APP_NAME
from utils.functions import clear


class PlayersView:
    def __init__(self, title):
        self.title = title

    def main_display(self):
        clear()
        print(f"[{APP_NAME}]\n")
        print(f"{self.title}\n")

    def list(self, players):
        self.main_display()
        for player in players:
            print(player)
