"""
Инициализация основного функционала аудиоплеера

Доступные классы:
- AudioPlayer (из core/audio/audio_control.py)
- PlaybackController (из core/audio/playback.py) 
- ExtractMeta (из core/metadata/reader.py)
- PlaylistBrowser (из core/playlist/browser.py)
- Utilities (из core/utils/utils.py)
"""

# Audio функционал
from .core.audio.audio_control import AudioPlayer

# Метаданные
from .core.metadata.reader import ExtractMeta

# Плейлисты
from .core.playlist.browser import PlaylistBrowser

# Утилиты
from .core.utils.helpers import Utilities

__all__ = [
    'AudioPlayer',
    'ExtractMeta', 
    'PlaylistBrowser',
    'Utilities'
]