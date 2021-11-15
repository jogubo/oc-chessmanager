from utils.constants import APP_NAME
from utils.functions import clear, prompt


class MenuView:
    def __init__(self, menu, title):
        self.menu = menu
        self.title = title

    @property
    def display(self):
        clear()
        print(f"[{APP_NAME}]\n")
        print(f"{self.title}\n")
        for key, value in self.menu.entries.items():
            print(f"[{key}] : {value}")
        print("")

    def user_choice(self):
        while True:
            self.display
            choice = prompt("Entrez le choix correspondant :").upper()
            if choice in self.menu.entries:
                return self.menu.entries[choice]
            else:
                print("Choix incorrect")
                # DEBUG
                print(type(self.menu.entries))
                print(self.menu.entries)
