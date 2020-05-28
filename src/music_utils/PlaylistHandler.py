import os
from src.music_utils.Song import Playlist, Song


def create_music_playlist(name):

    my_playlist = Playlist(name=name)
    PATH_TO_MUSIC_LIB = os.path.join(os.getcwd(), r'music_utils\music_lib')

    for file in os.listdir(PATH_TO_MUSIC_LIB):
        if file.endswith(".mp3"):
            my_playlist.songs.append(Song(os.path.join(PATH_TO_MUSIC_LIB, file)))

    return my_playlist


def find_song(song, playlist):
    i = 0
    for s in playlist.songs:
        if s.song_name == song.song_name:
            return i

        i += 1
    return i

