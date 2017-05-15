
from PyQt5.QtWidgets import (QMainWindow,
                             QWidget,
                             QDesktopWidget,
                             QTabWidget,
                             QHBoxLayout,
                             QVBoxLayout)
from cutepy.project_template.settings import CANVAS as ui


class BaseMainMenu(QMainWindow):

    width = ui['width']
    height = ui['height']
    pos_x = ui['x']
    pos_y = ui['y']

    def __init__(self, parent):
        super(BaseMainMenu, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.status_bar = self.statusBar()
        self.menu_bar = self.menuBar()
        self.setGeometry(self.pos_x, self.pos_y, self.width, self.height)
        self.show()

    def create(self, widget):
        self.setCentralWidget(widget)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        self.setWindowTitle(self._title)

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
        self.status_bar.showMessage(self._message)


class BaseWindow(QWidget):

    def __init__(self, parent=None):
        super(BaseWindow, self).__init__(parent)
        self.tab = QTabWidget()
        self.init_ui()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def create(self, width, height, title):
        self.resize(width, height)
        self.__center()
        self.show()

    def init_ui(self):
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()


class BaseWidget(QWidget):
    name = ""

    def __init__(self, parent=None):
        super(BaseWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        if self.name != "":
            self.setWindowTitle(self.name)
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
