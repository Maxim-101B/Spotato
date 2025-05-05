from pygame import mixer
import pygame

class AudioPlayer:
    def __init__(self):
        mixer.init()
        self.is_playing = False
        self.start_time = 0
        self.paused_position = 0  # Реальная позиция при паузе


    def load_audio_file(self, audio_file):
        try:
            mixer.music.load(audio_file)
            self.paused_position = 0  # Сброс при загрузке нового файла
        except pygame.error as e:
            raise Exception(f"Failed to load audio: {e}")


    def toggle_play_pause(self):
        if not self.is_playing:
            if self.start_time > 0:
                mixer.music.play(start=self.start_time)
            else:
                mixer.music.play()
            self.is_playing = True

        else:
            self.paused_position = mixer.music.get_pos() / 1000  # В секундах
            self.start_time += self.paused_position
            print(f'Прошло с начала {self.start_time}')
            mixer.music.pause()
            self.is_playing = False


    def get_current_time(self):
        if self.is_playing:
            ms = mixer.music.get_pos()
            sec = round(ms / 1000)
            now = sec + round(self.start_time)
            return now 
        else:
            return self.start_time


    def set_position(self, seconds):
        if self.is_playing:
            mixer.music.stop()
            mixer.music.play(start=seconds)
        else:
            self.paused_position = seconds






#            print('C начала:', self.start_time)
#            print('C начала ОКР:', round(self.start_time))
#            print("MS:", ms)
#            print('SEC:', sec)