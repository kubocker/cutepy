APP_TEMPLATE = """
import sys
from PyQt5.QtWidgets import QApplication
from menu import MainMenu


def main():
    app = QApplication(sys.argv)
    menu = MainMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
"""

MENU_TEMPLATE = """
from cutepy.base.menu import BaseMainMenu

class MainMenu(BaseMainMenu):

    def __init__(self):
        super().__init__()

    def init_ui(self):
        super().init_ui()
"""

APP_FORM_TEMPERATE = """
# Create your forms here.
"""

APP_VIEW_TEMPLATE = """
# Create your views here.
"""

APP_MODEL_TEMPLATE = """
# Create your models here.
"""
