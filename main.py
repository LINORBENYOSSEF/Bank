import sys

from PyQt5.QtWidgets import QApplication

from consts import RESOLUTION
from db.authentication import Authentication
from db.database import Database
from ui.accountview import AccountDisplay
from ui.login import LoginDisplay
from ui.newtransactionview import NewTransactionDisplay
from ui.window import MainWindow


def main():
    db = Database()
    authentication = Authentication(db)

    app = QApplication(sys.argv)
    newtrans = lambda: NewTransactionDisplay(db, authentication)
    mainmenu = lambda: AccountDisplay(authentication, newtrans)
    login = lambda: LoginDisplay(authentication, mainmenu)

    window = MainWindow(authentication)
    window.setFixedSize(RESOLUTION)
    # start the system
    window.start(login)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
