import enum
import os
import shutil
import threading

from kivy.core.audio import SoundLoader

from src.music_utils.Song import Song
from src.network import ClientManeger


class PlayQueue:
    def __init__(self):
        self.playlist = ClientManeger.server_songs if ClientManeger.is_online else ClientManeger.my_songs

        self.current = Song()
        self.next = self.current
        self.prev = self.current

        self.song_index = 0

        self.state = State.PAUSE

        self.audio_file = SoundLoader.load(self.current.file_name)

        self.dict = os.path.join(os.getcwd(), 'music_utils', 'music_lib', 'mus_cache')
        try:
            os.makedirs(self.dict)
        except FileExistsError:
            shutil.rmtree(self.dict)
            os.makedirs(self.dict)

        self.is_loading = False

    def string(self):
        return "Current: {}\nPrev: {}\nNext: {}".format(self.current, self.current, self.next)

    def set_state(self, new_state):
        if new_state is self.state:
            return

        if new_state is State.PAUSE:
            self.audio_file.stop()
            self.state = new_state

        elif new_state is State.PLAY:
            self.audio_file.play()
            self.state = new_state

    def toggle_state(self, *args):
        if self.audio_file is None:
            self.load_song_from_server(0)

        if self.is_loading:
            return

        else:
            self.set_state(State.PAUSE if self.state is State.PLAY else State.PLAY)
            ClientManeger.log.write("Action - PlayPause")

    def skip(self, *args):
        if self.audio_file is None:
            self.toggle_state()

        if self.is_loading:
            return

        else:
            self.unload()
            self.song_index += 1
            self.load_song_from_server(self.song_index)
            ClientManeger.log.write("Action - NextSong")

    def back(self, *args):
        if self.audio_file is None:
            self.toggle_state()

        if self.is_loading:
            return

        else:
            self.unload()
            self.song_index -= 1
            self.load_song_from_server(self.song_index)
            ClientManeger.log.write("Action - PrevSong")

    def is_playing(self):
        return self.state is State.PLAY

    def unload(self):
        if self.audio_file is not None:
            self.is_loading = True
            self.set_state(State.PAUSE)
            self.audio_file.unload()

    def load(self, play=True):
        self.audio_file = SoundLoader.load(self.current.file_name)
        if play:
            self.set_state(State.PLAY)
        self.is_loading = False

        auto_play_thread = threading.Thread(target=self.auto_play)
        auto_play_thread.start()

    def manege_cache(self, unload=True):
        path = os.path.join(self.dict, "stream.mp3")
        music_file = open(path, 'ab')

        if self.audio_file is not None:
            if unload:
                self.unload()
                music_file.truncate()

            return music_file.name

        else:
            return music_file.name

    def delete_cache(self):
        self.unload()
        shutil.rmtree(self.dict)

    def load_song_from_server(self, index):
        if ClientManeger.is_online:
            if self.audio_file is not None:
                self.unload()
            self.song_index = index
            self.playlist.songs[index].file_name = ClientManeger.req_song(index)
            self.set_current(index)
            self.load()
            
    def set_current(self, index):
        self.current = self.playlist.songs[index]

    def auto_play(self):
        if ClientManeger.is_online:
            while not self.is_loading:
                if self.audio_file.length - self.audio_file.get_pos() < 0.3339 and self.is_playing():
                    self.skip()
                else:
                    pass


class State(enum.Enum):
    PLAY = 1
    PAUSE = 0
