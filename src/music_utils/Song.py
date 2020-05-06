import enum
import os
from kivy.core.audio import SoundLoader


class Song:
    def __init__(self, song_name, artist, file_name):
        self.song_name = song_name
        self.artist = artist
        self.file_name = file_name

        self.audio_file = SoundLoader.load(self.file_name)

        self.state = State.PAUSE
        self.set_state(self.state)

    def string(self):
        return "Name: {}\nFrom: {}\nLocated: {}".format(self.song_name, self.artist, self.file_name)

    def set_state(self, new_state):
        if new_state is self.state:
            return

        if new_state is State.PAUSE:
            self.audio_file.stop()
            self.state = new_state

        elif new_state is State.PLAY:
            self.audio_file.play()
            self.state = new_state

    def delete(self):
        os.remove(self.file_name)
        self.song_name = ''
        self.artist = ''
        self.file_name = ''


class Playlist:
    def __init__(self, songs=[], name="MyPlaylist"):
        self.songs = songs
        self.name = name
    
    def string(self):
        string = "This playlist has {} songs:\n".format(len(self.songs))
        for song in self.songs:
            string += '\n' + song.string() + '\n'
        
        return string


class State(enum.Enum):
    PLAY = 1
    PAUSE = 0
