from src.music_utils.Song import Playlist, Song
from src.network.NetworkCommunication import *
from src.network.OperationType import OperationType
import os

server_songs = Playlist()
socket = None
log = None


def init(sock, logger):
    global socket
    socket = sock
    global log
    log = logger


def do_req(req, socket, log):
    pass


def get_all_server_songs():
    send_req(assemble_req(OperationType.ALL_SONGS.name), socket, log)
    server_msg_raw = recv_req(socket, log)
    server_msg_raw = server_msg_raw[len(OperationType.ALL_SONGS.name) + len(SEPARATOR_CHAR) + 1: len(server_msg_raw) - len(SEPARATOR_CHAR)]
    server_msg_raw = server_msg_raw.replace("'", "")

    global server_songs
    server_songs.conv_to_obj(playlist=server_msg_raw.split(","), name="ServerAllSongs")


def search_song(search):
    send_req(assemble_req(OperationType.SEARCH.name, search), socket, log)
    s_bytes = recv_req(socket, log, decode=False)

    path = os.path.join(os.getcwd(), 'music_utils', 'music_lib', 'temp')
    try:
        os.makedirs(path)

    except FileExistsError as err:
        log.write("an error occurred: {}".format(err))

    path = os.path.join(path, "stream.mp3")
    music_file = open(path, 'wb')
    music_file.write(s_bytes)


def disconnect():
    send_req(assemble_req(OperationType.DISCONNECT.name), socket, log)
