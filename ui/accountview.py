from typing import Callable, List

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

from consts import LABEL_STYLE, BUTTON_SIZE_3
from db.authentication import Authentication
from model.account import Transaction
from ui.shared import TopFrame
from ui.window import Display


class AccountDisplay(Display):

    def __init__(self, authentication: Authentication, newtrans_view: Callable[[], Display]):
        super().__init__()

        self._authentication = authentication
        self._newtrans_view = newtrans_view

        self._top = TopFrame(self.on_logout)
        account_data = self._create_account_data()
        self._transaction_history_layout = QTableWidget()

        self.newtrans_button = QPushButton('New Transaction')
        self.newtrans_button.setFixedSize(BUTTON_SIZE_3)
        self.newtrans_button.clicked.connect(self._newtrans)

        root_layout = QVBoxLayout()
        root_layout.addWidget(self._top, alignment=Qt.AlignTop)
        root_layout.addLayout(account_data)
        root_layout.addWidget(self._transaction_history_layout, alignment=Qt.AlignCenter)
        root_layout.addWidget(self.newtrans_button, alignment=Qt.AlignBottom)
        self.setLayout(root_layout)

    def prepare_show(self):
        self._top.set_default_welcome_text(self._authentication)

        account = self._authentication.current_account
        self._account_number_field.setText(str(account.account_number))
        self._account_balance_field.setText(str(account.balance))

        self.load_transaction_history(account.transactions)

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

    def load_transaction_history(self, transactions: List[Transaction]):
        self._transaction_history_layout.setRowCount(len(transactions))
        self._transaction_history_layout.setColumnCount(4)

        self._transaction_history_layout.setHorizontalHeaderLabels(['Direction', 'Datetime', 'Account Number', 'Amount [$]'])

        for row in range(len(transactions)):
            transaction = transactions[row]
            self._transaction_history_layout.setItem(row, 0, QTableWidgetItem(transaction.direction))
            str_datetime = transaction.datetime.strftime('%d/%m/%Y %H:%M:%S')
            self._transaction_history_layout.setItem(row, 1, QTableWidgetItem(str_datetime))
            self._transaction_history_layout.setItem(row, 2, QTableWidgetItem(str(transaction.dest_account)))
            self._transaction_history_layout.setItem(row, 3, QTableWidgetItem(str(transaction.amount)))

    def _newtrans(self):
        self.on_next.emit(self._newtrans_view)
