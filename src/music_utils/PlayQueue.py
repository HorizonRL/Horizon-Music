from src.music_utils.Song import Song, Playlist


class PlayQueue:
    def __init__(self):
        self.playlist = Playlist()
        self.current = Song('')
        self.next = self.current
        self.prev = self.current
        self.song_index = 0

    def set_current_song(self, current):
        self.current = current
        index = 0
        for song in self.playlist.songs:
            if self.current == song:
                self.song_index = index
                self.update()
                return
            index += 1

    def update(self):
        self.prev = self.playlist.songs[self.song_index - 1]
        self.next = self.playlist.songs[self.song_index + 1]

    def string(self):
        return "Current: {}\nPrev: {}\nNext: {}".format(self.current, self.current, self.next)
