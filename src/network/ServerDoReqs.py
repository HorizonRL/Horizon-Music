from src.music_utils.PlaylistHandler import PlaylistHandler
from src.network.OperationType import OperationType
from src.network.NetworkCommunication import *

_playlist_handler = PlaylistHandler()


def do_req(req, socket, address, log):
    if req[0] == OperationType.ALL_SONGS.name:
        _send_all_song_playlist(socket, log)
    elif req[0] == OperationType.SEARCH.name:
        _search(req[1:], socket, log)
    elif req[0] == OperationType.DISCONNECT.name:
        _disconnect(socket, address, log)
    elif req[0] == OperationType.REQ_SONG.name:
        _send_song(req[1:], socket, log)


def _search(search, socket, log):
    # len\search\song(str)
    _send_song(search, socket, log)


def _send_song(song_to_play, socket, log):
    # len\send_song\song(str)
    index = 0
    song_index = 0
    for song in _playlist_handler.all_music.songs:
        if song.song_name is song_to_play:
            song_index = index
            break

        index += 1

    file = open(_playlist_handler.all_music.songs[song_index].song_file, "r").read()
    send_req(assemble_req(OperationType.REQ_SONG.name, file))


def _disconnect(socket, address, log):
    # len\disconnect
    log.write("{} disconnecting".format(address))
    socket.close()


def _send_all_song_playlist(socket, log):
    # len\all_songs
    send_req(assemble_req(OperationType.ALL_SONGS.name, _playlist_handler.all_music.string()), socket, log)
