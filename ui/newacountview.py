from typing import Callable, List

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

from consts import LABEL_STYLE, BUTTON_SIZE_3
from db.authentication import Authentication
from model.account import Transaction
from ui.shared import TopFrame
from ui.window import Display


class AccountDisplay(Display):

    def __init__(self, authentication: Authentication, mainview: Callable[[], Display]):
        super().__init__()

        self._authentication = authentication
        self._mainview = mainview

        self._top = TopFrame(self.on_logout)
        account_data = self._create_account_data()
        self._transaction_history_layout = QTableWidget()

        self.create_button = QPushButton('Create')
        self.create_button.setFixedSize(BUTTON_SIZE_3)
        self.create_button.clicked.connect(self._on_create)
        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.setFixedSize(BUTTON_SIZE_3)
        self.cancel_button.clicked.connect(self._on_cancel)

        root_layout = QVBoxLayout()
        root_layout.setAlignment(Qt.AlignCenter)
        root_layout.addWidget(self._top, alignment=Qt.AlignTop)
        root_layout.addLayout(account_data)
        root_layout.addWidget(self.create_button, alignment=Qt.AlignCenter)
        root_layout.addWidget(self.cancel_button, alignment=Qt.AlignCenter)
        self.setLayout(root_layout)

    def prepare_show(self):
        self._top.set_default_welcome_text(self._authentication)

        account = self._authentication.current_account
        self._name_field.setText(str(account.account_number))
        self._account_balance_field.setText(str(account.balance))

        self.load_transaction_history(account.transactions)

    def _create_account_data(self):
        form_layout = QFormLayout()
        form_layout.setAlignment(Qt.AlignCenter)

        label_size = QSize(120, 20)
        field_size = QSize(170, 30)

        label = QLabel('Name')
        label.setStyleSheet(LABEL_STYLE)
        label.setFixedSize(label_size)
        self._name_field = QLineEdit()
        self._name_field.setReadOnly(False)
        self._name_field.setFixedSize(field_size)
        form_layout.addRow(label, self._name_field)

        label = QLabel('Balance')
        label.setStyleSheet(LABEL_STYLE)
        label.setFixedSize(label_size)
        self._account_balance_field = QLineEdit()
        self._account_balance_field.setReadOnly(False)
        self._account_balance_field.setFixedSize(field_size)
        form_layout.addRow(label, self._account_balance_field)

        return form_layout

    def _on_create(self):
        pass

    def _on_cancel(self):
        self.on_back.emit()
