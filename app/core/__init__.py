"""
Инициализация основного функционала аудиоплеера

Доступные классы:
- AudioPlayer (из audio/audio_control.py)
- PlaybackController (из audio/playback.py) 
- ExtractMeta (из metadata/reader.py)
- PlaylistBrowser (из playlist/browser.py)
- Utilities (из utils/utils.py)
"""

# Audio функционал
from .audio.audio_control import AudioPlayer

# Метаданные
from .metadata.reader import ExtractMeta

# Плейлисты
from .playlist.browser import PlaylistBrowser

# Утилиты
from .utils.helpers import Utilities

__all__ = [
    'AudioPlayer',
    'ExtractMeta', 
    'PlaylistBrowser',
    'Utilities'
]