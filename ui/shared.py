from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout

from db.authentication import Authentication
from consts import LABEL_STYLE, UNDERLINE_LABEL_STYLE


class TopFrame(QFrame):

    def __init__(self, on_logout):
        super().__init__()

        top_layout = QHBoxLayout()

        label = QLabel('Logout')
        label.setCursor(QCursor(Qt.PointingHandCursor))
        label.setStyleSheet(UNDERLINE_LABEL_STYLE)
        label.mousePressEvent = lambda e: on_logout.emit()
        top_layout.addWidget(label)

        top_layout.addStretch()

        self._hello_label = QLabel()
        self._hello_label.setStyleSheet(LABEL_STYLE)
        top_layout.addWidget(self._hello_label)

        self.setLayout(top_layout)

    def set_welcome_text(self, text: str):
        self._hello_label.setText(text)

    def set_default_welcome_text(self, authentication: Authentication):
        self.set_welcome_text(f"Account: {authentication.current_account.account_number}")

