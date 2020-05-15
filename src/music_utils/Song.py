import enum
import os
from kivy.core.audio import SoundLoader


class Song:
    def __init__(self, file):
        self.file_name = file

        sep_index = file.find('-')
        lib_folder = "music_lib"

        if file is not '':

            self.song_name = file[sep_index + 1 if file[sep_index + 1] is not ' ' else sep_index + 2:
                                  file.find('.mp3')].title()

            self.artist = file[file.find(lib_folder) + len(lib_folder) + 1:
                               sep_index if file[sep_index - 1] is not ' ' else sep_index - 1].title()

            self.audio_file = SoundLoader.load(self.file_name)

        else:

            self.song_name = ""
            self.artist = ""

        self.state = State.PAUSE
        self.set_state(self.state)
        self.is_local = False

    def string(self):
        return "{} | {}".format(self.song_name, self.artist)

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
        string = []
        for song in self.songs:
            string.append(song.string())
        
        return string

    def conv_to_obj(self, playlist=[], name='MyPlaylist'):
        self.name = name
        for song in playlist:
            the_song = Song('')
            the_song.song_name = song[: song.find('|') - 1]
            the_song.artist = song[song.find('|') + 1:]
            self.songs.append(the_song)


class State(enum.Enum):
    PLAY = 1
    PAUSE = 0
