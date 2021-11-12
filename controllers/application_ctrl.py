import sys
from controllers.home_menu_ctrl import HomeMenuCtrl


class ApplicationCtrl:

    @staticmethod
    def start():
        controller = HomeMenuCtrl()
        controller()

    @staticmethod
    def close():
        sys.exit()
