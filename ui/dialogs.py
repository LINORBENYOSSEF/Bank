import traceback

from PyQt5.QtWidgets import QMessageBox


def show_error_dialog(parent, error: Exception):
    dialog = QMessageBox(parent)
    dialog.setIcon(QMessageBox.Critical)
    dialog.setText(str(error))
    dialog.setWindowTitle('Error')
    dialog.setStandardButtons(QMessageBox.Ok)

    backtrace = traceback.format_exception(type(error), error, error.__traceback__)
    dialog.setDetailedText('\n '.join(backtrace))

    dialog.exec()
