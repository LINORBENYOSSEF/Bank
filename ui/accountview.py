from typing import Callable

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QLabel, QPushButton, QVBoxLayout, QFrame

from db.authentication import Authentication
from consts import LABEL_STYLE
from ui.shared import TopFrame
from ui.window import Display


class AccountDisplay(Display):

    def __init__(self, authentication: Authentication):
        super().__init__()

        self._authentication = authentication

        self._top = TopFrame(self.on_logout)
        account_data = self._create_account_data()

        root_layout = QVBoxLayout()
        root_layout.addWidget(self._top, alignment=Qt.AlignTop)
        root_layout.addWidget(account_data, alignment=Qt.AlignCenter)
        self.setLayout(root_layout)

    def prepare_show(self):
        self._top.set_default_welcome_text(self._authentication)

        account = self._authentication.current_account
        self._account_number_field.setText(account.account_number)
        self._account_balance_field.setText(account.balance)

    def _create_account_data(self):
        form_layout = QFormLayout()
        form_layout.setAlignment(Qt.AlignCenter)

        label_size = QSize(70, 20)
        field_size = QSize(170, 30)

        label = QLabel('Account Number')
        label.setStyleSheet(LABEL_STYLE)
        label.setFixedSize(label_size)
        self._account_number_field = QLineEdit()
        self._account_number_field.setReadOnly(True)
        self._account_number_field.setFixedSize(field_size)
        form_layout.addRow(label, self._account_number_field)

        label = QLabel('Balance')
        label.setStyleSheet(LABEL_STYLE)
        label.setFixedSize(label_size)
        self._account_balance_field = QLineEdit()
        self._account_balance_field.setReadOnly(True)
        self._account_balance_field.setFixedSize(field_size)
        form_layout.addRow(label, self._account_balance_field)

        return form_layout

