#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from base.menu import BaseMainMenu


def main():
    app = QApplication(sys.argv)
    menu = BaseMainMenu()
    # menu.title = "テスト"
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
