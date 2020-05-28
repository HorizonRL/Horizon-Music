import os


class Song:
    def __init__(self, file=''):
        self.file_name = file

        sep_index = file.find('-')
        lib_folder = "music_lib"

        if file is not '':

            self.song_name = file[sep_index + 1 if file[sep_index + 1] is not ' ' else sep_index + 2:
                                  file.find('.mp3')].title()

            self.artist = file[file.find(lib_folder) + len(lib_folder) + 1:
                               sep_index if file[sep_index - 1] is not ' ' else sep_index - 1].title()

        else:
            self.song_name = ""
            self.artist = ""

    def string(self):
        return "{} | {}".format(self.song_name, self.artist)

    def delete(self):
        os.remove(self.file_name)
        self.song_name = ''
        self.artist = ''
        self.file_name = ''


class Playlist:
    def __init__(self, songs=[], name="MyPlaylist"):
        self.songs = []
        self.name = name
    
    def string(self):
        string = []
        for song in self.songs:
            string.append(song.string())
        
        return string

    def conv_to_obj(self, playlist=[], name='MyPlaylist'):
        self.name = name
        i = 0
        for song in playlist:
            s = Song('')
            s.song_name = song[: song.find('|') - 1].replace('"', "").replace(']', '')
            s.artist = song[song.find('|') + 1:].replace('"', "").replace(']', '')
            self.songs.insert(i, s)
            i += 1
