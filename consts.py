from pathlib import Path

from PyQt5.QtCore import QSize


RESOLUTION = QSize(700, 400)


RESOURCES_PATH = Path('resources')
LOADING_SPINNER = RESOURCES_PATH / 'ajax-loader.gif'
BACKGROUND = RESOURCES_PATH / 'backWithLogo.png'
BACKGROUND_BLUE = RESOURCES_PATH / 'back_without_logo.png'

LABEL_STYLE = "color: black; font-weight: bold;"
UNDERLINE_LABEL_STYLE = "text-decoration: underline;" + LABEL_STYLE
BUTTON_SIZE_3 = QSize(170, 40)
BUTTON_SIZE_4 = QSize(120, 40)
