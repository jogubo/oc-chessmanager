from utils.functions import clear, prompt
from utils.constants import APP_NAME


class HomeView:

    title = "Menu Principal"

    @classmethod
    def main_display(cls):
        clear()
        print(f"[{APP_NAME}]\n")
        print(f"{cls.title}\n")

    @classmethod
    def display_menu(cls, menu):
        while True:
            cls.main_display()
            for key, value in menu.items():
                print(f"[{key}] : {value['menu_title']}")
            user_choice = prompt("Entrez le choix correspondant :").upper()
            if user_choice in menu:
                return menu[user_choice]['route']
