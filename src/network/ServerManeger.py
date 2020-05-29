from src.music_utils.PlaylistHandler import create_music_playlist
from src.network.OperationType import OperationType
from src.network.NetworkCommunication import *

all_music = create_music_playlist("All Songs")
socket = None
log = None


def init(sock, logger):
    global socket
    socket = sock
    global log
    log = logger


def do_req(req, address):
    if req[0] == OperationType.ALL_SONGS.name:
        _send_all_song_playlist()
        return

    elif req[0] == OperationType.DISCONNECT.name:
        _disconnect(address)
        return

    elif req[0] == OperationType.REQ_SONG.name:
        _send_song(req[1:])
        return

    else:
        return


def _disconnect(address):
    log.write("{} disconnecting".format(address))
    socket.close()


def _send_all_song_playlist():
    send_req(assemble_req(OperationType.ALL_SONGS.name, all_music.string()), socket, log)


def _send_song(song_index):
    i = int(song_index[0])
    file = open(all_music.songs[i].file_name, "rb")
    send_req(file.read(), socket, log, encode=False)
    file.close()
