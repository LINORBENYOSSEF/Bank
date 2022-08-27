from pathlib import Path
from typing import Callable

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget

from db.authentication import Authentication
from consts import BACKGROUND


class Display(QWidget):
    on_logout = pyqtSignal()
    on_back = pyqtSignal()
    on_next = pyqtSignal(object)
    switch_background = pyqtSignal(object)

    def prepare_show(self):
        pass


class MainWindow(QMainWindow):
    _STYLESHEET_FORMAT = """
    MainWindow {{
        border-image: url("{background}");
    }}
    QPushButton {{
        background-color: #6898FF; 
        color: white; 
        font-weight: bold; 
        border-radius: 20%;
    }}
    """

    def __init__(self, authentication: Authentication):
        super().__init__()

        self._authentication = authentication

        self._last_factory = None
        self._current_factory = None
        self._current = None
        self._logout_target = None

        self.setWindowTitle('Rumor Detector')
        self._switch_background(BACKGROUND)

    def start(self, enter: Callable[[], Display]):
        self._logout_target = enter
        self._on_window_change(enter)
        self.show()

    def _on_window_change(self, next_factory: Callable[[], Display]):
        if self._current is not None:
            self._current.on_logout.disconnect(self._on_logout)
            self._current.on_back.disconnect(self._on_back)
            self._current.on_next.disconnect(self._on_next)
            self._current.switch_background.disconnect(self._switch_background)

        self._last_factory = self._current_factory
        self._current_factory = next_factory

        self._current = next_factory()

        self._current.on_logout.connect(self._on_logout)
        self._current.on_back.connect(self._on_back)
        self._current.on_next.connect(self._on_next)
        self._current.switch_background.connect(self._switch_background)

        self._current.prepare_show()
        self.setCentralWidget(self._current)

    def _on_logout(self):
        self._authentication.logout()
        self._on_window_change(self._logout_target)

    def _on_back(self):
        self._on_window_change(self._last_factory)

    def _on_next(self, next_factory: Callable[[], Display]):
        self._on_window_change(next_factory)

    def _switch_background(self, background_path: Path):
        path = str(background_path).replace('\\', '/')
        self.setStyleSheet(self._STYLESHEET_FORMAT.format(background=path))
