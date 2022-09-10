from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QLabel, QVBoxLayout, QPushButton

from consts import LABEL_STYLE, BUTTON_SIZE_3
from db.authentication import Authentication
from db.database import Database
from db.transaction import do_transaction
from ui.shared import TopFrame
from ui.window import Display
from ui.dialogs import show_error_dialog


class NewTransactionDisplay(Display):

    def __init__(self, db: Database, authentication: Authentication):
        super().__init__()

        self._db = db
        self._authentication = authentication

        self._top = TopFrame(self.on_logout)

        transaction_form = self._create_form()

        self.back_button = QPushButton('Back')
        self.back_button.setFixedSize(BUTTON_SIZE_3)
        self.back_button.clicked.connect(self._on_back)

        self.save_button = QPushButton('Save')
        self.save_button.setFixedSize(BUTTON_SIZE_3)
        self.save_button.setDisabled(True)
        self.save_button.clicked.connect(self._on_save)

        root_layout = QVBoxLayout()
        root_layout.addWidget(self._top, alignment=Qt.AlignTop)
        root_layout.addLayout(transaction_form)
        root_layout.addWidget(self.save_button, alignment=Qt.AlignBottom)
        root_layout.addWidget(self.back_button, alignment=Qt.AlignBottom)
        self.setLayout(root_layout)

    def prepare_show(self):
        self._top.set_default_welcome_text(self._authentication)
        self._account_number_field.setText('')
        self._amount_field.setText('0.0')
        self.save_button.setDisabled(True)

    def _create_form(self):
        form_layout = QFormLayout()
        form_layout.setAlignment(Qt.AlignCenter)

        label_size = QSize(70, 20)
        field_size = QSize(170, 30)

        label = QLabel('Account Number')
        label.setStyleSheet(LABEL_STYLE)
        label.setFixedSize(label_size)
        self._account_number_field = QLineEdit()
        self._account_number_field.setFixedSize(field_size)
        self._account_number_field.textChanged.connect(self._text_changed)
        form_layout.addRow(label, self._account_number_field)

        label = QLabel('Amount')
        label.setStyleSheet(LABEL_STYLE)
        label.setFixedSize(label_size)
        self._amount_field = QLineEdit()
        self._amount_field.setFixedSize(field_size)
        self._amount_field.textChanged.connect(self._text_changed)
        form_layout.addRow(label, self._amount_field)

        return form_layout

    def _text_changed(self, *args):
        is_input_valid = self.is_int(self._account_number_field.text()) > 0 and \
                         self.is_float(self._amount_field.text())
        self.save_button.setDisabled(not is_input_valid)

    def _on_back(self):
        self.on_back.emit()

    def _on_save(self):
        try:
            dst_account_number = int(self._account_number_field.text())
            amount = float(self._amount_field.text())
            do_transaction(self._db, self._authentication.current_account, dst_account_number, amount)

            self._account_number_field.setText('')
            self._amount_field.setText('0.0')
            self.save_button.setDisabled(True)
        except Exception as e:
            show_error_dialog(self, e)

    def is_float(self, value: str):
        return value.isdecimal()

    def is_int(self, value: str):
        return value.isdigit()
