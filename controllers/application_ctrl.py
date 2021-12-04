import sys
from controllers.home_ctrl import HomeCtrl


class ApplicationCtrl:

    @staticmethod
    def start():
        controller = HomeCtrl.display_menu()
        controller()

    @staticmethod
    def close():
        sys.exit()
