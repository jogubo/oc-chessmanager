class MenuEntry:
    def __init__(self, option, controller):
        self._option = option
        self._controller = controller

    def __repr__(self):
        return self._option

    @property
    def controller(self):
        return self._controller
