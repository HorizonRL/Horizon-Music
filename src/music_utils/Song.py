import enum
import os

class Song:
    def __init__(self, song_name, artist, file_name, song_format='.mp3'):
        self.song_name = song_name
        self.artist = artist
        self.file_name = file_name
        self.song_format = song_format

        self.state = State.PAUSE

    def string(self):
        return "Name: {}\nFrom: {}\nLocated: {}".format(self.song_name, self.artist, self.file_name)

    def set_state(self, state):
        if state is self.state:
            return

        if state is State.PAUSE:
            pass

        elif state is State.PLAY:
            pass

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
