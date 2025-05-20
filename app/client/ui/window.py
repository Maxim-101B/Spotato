import os
from PySide6.QtWidgets import QMainWindow, QFileDialog, QSizePolicy
from PySide6.QtCore import QTimer, Qt

from .ui_main import Ui_MainWindow
from app.core import ExtractMeta, AudioPlayer, PlaylistBrowser, Utilities

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.extractor = ExtractMeta()
        self.player = AudioPlayer()
        self.utils = Utilities()
        self.playlist_browser = PlaylistBrowser()