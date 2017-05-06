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
from PyQt5.QtWidgets import *
from cutepy.base.menu import BaseMainMenu, BaseWindow
from {0} import settings


class MainWindow(BaseWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    def init_ui(self):
        super().init_ui()
        h_box = QHBoxLayout()
        for k in range(len(settings.INSTALLED_APPS)):
            print(settings.INSTALLED_APPS[k])
            self.tab.addTab(QWidget(), settings.INSTALLED_APPS[k])
        h_box.addWidget(self.tab)
        self.setLayout(h_box)
        self.show()


class MainMenu(BaseMainMenu):

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)

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
