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
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.set_crnt_time)
        
        self.is_playing = False
        
        self.ui.playback_btn.setEnabled(False)
        self.ui.SelectAudioBtn.clicked.connect(self.select_song)
        self.ui.playback_btn.pressed.connect(self.toggle_playback)


    def set_dir(self, directory):
        self.dir = directory

    def select_song(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Выберите аудиофайл', '', 'Audio Files (*.mp3)'
        )

        self.set_dir(file_path)
        file_name = os.path.basename(file_path)

        if file_path:
            metadata = self.extractor.extract_meta(file_path)
            self.display_music_info(metadata, file_name)
            self.player.load_audio_file(file_path)
            self.ui.playback_btn.setEnabled(True)

    def display_music_info(self, metadata, file_name):
        metadata_str = '\n'.join(metadata)
        self.ui.CurrentFile_lb.setText('Выбран аудиофайл:')
        self.ui.CurrentFile.setText(file_name)
        self.set_track_length()

        if str.strip(metadata_str):
            self.ui.TrackInfo.setText(metadata_str)
        else:
            self.ui.TrackInfo.setText("Метаданные отсутствуют")

    def toggle_playback(self):
        self.is_playing = not self.is_playing 
        self.player.toggle_play_pause()
        self.timer.start(1000) if self.is_playing else self.timer.stop()

    def set_track_length(self):
        file_path = self.dir
        audio_lengh = self.extractor.get_audio_length(file_path)
        formatted_length = self.utils.seconds_to_mm_ss(audio_lengh)
        self.ui.EndTime.setText(formatted_length)
        return audio_lengh

    def set_crnt_time(self):
        crnt_time = self.player.get_current_time()
        formatted_crnt_time = self.utils.seconds_to_mm_ss(crnt_time)

        if crnt_time is not None:
            self.ui.CurrentTime.setText(formatted_crnt_time)
            print(formatted_crnt_time)
        else:
            self.ui.CurrentTime.setText("00:00")