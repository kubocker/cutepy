import sys
from PyQt5.QtWidgets import QApplication
from .menu import MainMenu


def main():
    app = QApplication(sys.argv)
    menu = MainMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
