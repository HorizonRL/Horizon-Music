import enum
from kivy.core.audio import SoundLoader

from src.music_utils.Song import Song, Playlist


class PlayQueue:
    def __init__(self):
        self.playlist = Playlist()

        self.current = Song('')
        self.next = self.current
        self.prev = self.current

        self.song_index = 0

        self.state = State.PAUSE

        self.audio_file = None

    def set_current_song(self, current, file):
        self.current = current
        index = 0
        for song in self.playlist.songs:
            if self.current.song_name == song.song_name:
                self.song_index = index
                self.audio_file = SoundLoader.load(file)
                self.update()
                return
            index += 1

    def update(self):
        self.set_state(State.PAUSE)
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


class State(enum.Enum):
    PLAY = 1
    PAUSE = 0
