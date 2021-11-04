from utils import constants
from utils import functions


class MenuView:
    def __init__(self, menu, title):
        self.menu = menu
        self.title = title

    @property
    def display(self):
        functions.clear()
        print(f"[{constants.TITLE}]\n")
        print(f"{self.title}\n")
        for key, value in self.menu.entries.items():
            print(f"[{key}] : {value}")

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
