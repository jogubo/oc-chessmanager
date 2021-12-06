from models.menu_entry import MenuEntry


class Menu:

    def __init__(self):
        self._entries = {}
        self._autokey = 1

    def add(self, key, option, controller):
        self._entries[str(key)] = MenuEntry(option, controller)

    @property
    def entries(self):
        return self._entries
