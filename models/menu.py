from models.menu_entry import MenuEntry


class Menu:

    def __init__(self):
        self._entries = {}
        self._autokey = 1

    def add(self, key, option, controller):
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1

        self._entries[str(key)] = MenuEntry(option, controller)

    @property
    def entries(self):
        return self._entries
    '''
    entries = {}
    autokey = 1

    def __init(self):
        pass

    def add(self, key, option, controller):
        self._option = option
        self._controller = controller
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1

    def __repr__(self):
        return self._option

    @property
    def controller(self):
        return self._controller

    @classmethod
    def add(cls, key, option, controller):
        if key == "auto":
            key = str(cls.autokey)
            cls.autokey += 1

        cls.entries[str(key)] = MenuEntry(option, controller)

    @classmethod
    def entries(cls):
        return cls.entries
    '''
