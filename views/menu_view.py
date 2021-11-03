from utils import constants
from os import system


class MenuView:
    def __init__(self, menu):
        self.menu = menu

    @property
    def display(self):
        system('clear')
        print(f"[{constants.TITLE}]\n")
        for key, value in self.menu.entries.items():
            print(f"{key} : {value}")

    @property
    def user_choice(self):
        while True:
            self.display
            print("\nEntrez le choix correspondant :")
            choice = input('>> ').upper()
            if choice in self.menu.entries:
                return self.menu.entries[choice]
            else:
                print("Choix incorrect")
                # DEBUG
                print(type(self.menu.entries))
                print(self.menu.entries)
