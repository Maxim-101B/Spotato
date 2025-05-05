from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


class ExtractMeta():
    def __init__(self):
        super(ExtractMeta, self).__init__()


    def extract_meta(self, audio_file):
        audio = EasyID3(audio_file)
        
        keys = audio.keys()
        song_info = []

        for key in keys:
            value = audio.get(key, ["Значение не найдено"])[0]
            song_info.append(f"{str.upper(key)}: {value}")
            

        return(song_info)
    

    def get_audio_length(self, file_path):
        audio = MP3(file_path)
        audio_length = int(audio.info.length)
        return str(audio_length) # Длина в формате (mm:ss)!!!


if __name__ == "__main__":
    ExtractMeta()






#artist = audio.get("artist", ["no_info"])[0]