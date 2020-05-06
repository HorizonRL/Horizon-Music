import os
from src.music_utils.Song import Playlist, Song


def create_all_music_playlist():
    my_playlist = Playlist(name="All Songs")
    PATH_TO_MUSIC_LIB = os.path.join(os.getcwd(), r'music_lib')
    for file in os.listdir(PATH_TO_MUSIC_LIB):
        if file.endswith(".mp3"):
            sep_index = file.find('-')
            artist = file[:sep_index if file[sep_index - 1] is not ' ' else sep_index - 1].title()
            name = file[sep_index + 1 if file[sep_index + 1] is not ' ' else sep_index + 2: file.find('.mp3')].title()

            my_playlist.songs.append(Song(name, artist, os.path.join(PATH_TO_MUSIC_LIB, file)))

    print(my_playlist.string())
    return my_playlist


class PlaylistHandler:
    def __init__(self):
        self.all_music = create_all_music_playlist()


if __name__ == '__main__':
    PlaylistHandler()
