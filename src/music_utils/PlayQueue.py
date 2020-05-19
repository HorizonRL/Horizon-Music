import enum
import os
import shutil

from kivy.core.audio import SoundLoader

from src.music_utils.Song import Song, Playlist
from src.network import ClientDoReqs


class PlayQueue:
    def __init__(self):
        self.playlist = Playlist()

        self.current = Song('')
        self.next = self.current
        self.prev = self.current

        self.song_index = 0

        self.state = State.PAUSE
        self.is_current_by_queue = False

        self.audio_file = None

        self.is_down_to_def_cache_file = True

        self.dict = os.path.join(os.getcwd(), 'music_utils', 'music_lib', 'mus_cache')
        try:
            os.makedirs(self.dict)
        except FileExistsError as err:
            pass

        self.next_path = None

    def set_current_song(self, current, file):
        if current.song_name == self.current.song_name:
            return

        if self.is_playing():
            self.audio_file.unload()

        self.current = current
        index = 0
        for song in self.playlist.songs:
            if self.current.song_name == song.song_name:
                self.song_index = index
                self.audio_file = SoundLoader.load(file)
                self.update()
                self.is_current_by_queue = False
                return
            index += 1

    def set_next(self, file):
        self.next_path = file

    def update(self):
        self.prev = self.playlist.songs[self.song_index - 1]
        self.next = self.playlist.songs[self.song_index + 1]

    def skip(self):
        self.set_state(State.PAUSE)
        self.prev = self.current
        self.current = self.next
        self.song_index += 1
        self.next = self.playlist.songs[self.song_index]

    def back(self):
        self.set_state(State.PAUSE)
        self.next = self.current
        self.current = self.prev
        self.song_index -= 1
        self.next = self.playlist.songs[self.song_index]

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

    def toggle_state(self):
        self.set_state(State.PAUSE if self.state is State.PLAY else State.PLAY)

    def is_playing(self):
        return self.state is State.PLAY

    def unload(self):
        self.set_state(State.PAUSE)
        self.audio_file.unload()

    def manege_cache(self, unload=True):
        names = ['stream', "stream1"]

        if self.is_down_to_def_cache_file:
            self.is_down_to_def_cache_file = False
            path = os.path.join(self.dict, "{}.mp3".format(names[0]))
            music_file = open(path, 'ab')
            music_file.truncate()

            if self.is_playing() and unload:
                self.unload()
                os.remove(path.replace(names[0], names[1]))

        else:
            self.is_down_to_def_cache_file = True
            path = os.path.join(self.dict, "{}.mp3".format(names[1]))
            music_file = open(path, 'ab')
            music_file.truncate()

            if self.is_playing() and unload:
                self.unload()
                os.remove(path.replace(names[1], names[0]))

        return music_file

    def delete_cache(self):
        shutil.rmtree(self.dict)

    def is_next_song(self):
        return self.is_playing() and (self.audio_file.get_pos() + 2 == self.audio_file.legnth)

    def auto_play_via_net(self):
        while True:
            if self.is_playing():
                if self.is_next_song():
                    ClientDoReqs.req_song(self.next)

                if self.audio_file.legnth - self.audio_file.get_pos < 0.2:
                    self.unload()
                    os.remove(self.current.file_name)
                    self.update()

                    self.audio_file = SoundLoader.load(self.next_path)
                    self.set_state(State.PLAY)


class State(enum.Enum):
    PLAY = 1
    PAUSE = 0
