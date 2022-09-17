from typing import Callable

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QLabel, QPushButton, QVBoxLayout, QFrame

from db.authentication import Authentication
from consts import LABEL_STYLE
from ui.window import Display


class LoginDisplay(Display):

    def __init__(self, authentication: Authentication, mainmenu: Callable[[], Display]):
        super().__init__()

        self._authentication = authentication
        self._mainmenu = mainmenu

        form = self._create_form()

        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(0, 100, 0, 0)
        root_layout.addWidget(form, alignment=Qt.AlignCenter)
        self.setLayout(root_layout)

    def prepare_show(self):
        self._account_number_field.clear()
        self._error_field.setText('')

    def _create_form(self):
        form_layout = QFormLayout()
        form_layout.setAlignment(Qt.AlignCenter)

        label_size = QSize(120, 20)
        field_size = QSize(170, 30)

        label = QLabel('Account Number')
        label.setStyleSheet(LABEL_STYLE)
        label.setFixedSize(label_size)
        self._account_number_field = QLineEdit()
        self._account_number_field.setFixedSize(field_size)
        form_layout.addRow(label, self._account_number_field)

        self._login_button = QPushButton("Log In")
        self._login_button.clicked.connect(self._login)
        self._login_button.setFixedSize(QSize(70, 30))
        form_layout.addWidget(self._login_button)

        self._error_field = QLabel()
        self._error_field.setStyleSheet('color: red; font-weight: bold')
        form_layout.addWidget(self._error_field)

        form = QFrame()
        form.setLayout(form_layout)
        return form

    def _login(self):
        try:
            account_number = int(self._account_number_field.text())

            self._authentication.login(account_number)
            self._error_field.setText('')

            self.on_next.emit(self._mainmenu)
        except Exception as e:
            self._error_field.setText(str(e))
