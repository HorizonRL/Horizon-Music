from src.music_utils.PlayQueue import PlayQueue, State
from src.music_utils.PlaylistHandler import create_music_playlist
from src.music_utils.Song import Playlist, Song
from src.network.NetworkCommunication import *
from src.network.OperationType import OperationType


from src.utils.Constants import GUIFiles

server_songs = Playlist()
my_songs = create_music_playlist("Downloads")

play_queue = None
gui_src = None
socket = None
log = None
is_online = False


def init(sock, logger, online):
    global socket
    socket = sock
    global log
    log = logger
    global gui_src
    gui_src = GUIFiles(log)
    global is_online
    is_online = online
    global play_queue
    play_queue = PlayQueue()
    

def get_all_server_songs():
    send_req(assemble_req(OperationType.ALL_SONGS.name), socket, log)
    server_msg_raw = recv_req(socket, log)
    server_msg_raw = server_msg_raw[len(OperationType.ALL_SONGS.name) + len(SEPARATOR_CHAR) + 1: len(server_msg_raw) - len(SEPARATOR_CHAR)]
    server_msg_raw = server_msg_raw.replace("'", "")

    global server_songs
    server_songs.conv_to_obj(playlist=server_msg_raw.split(","), name="ServerAllSongs")


def disconnect():
    play_queue.delete_cache()
    send_req(assemble_req(OperationType.DISCONNECT.name), socket, log)


def req_song(song_index):
    send_req(assemble_req(OperationType.REQ_SONG.name, song_index), socket, log)
    s_bytes = recv_req(socket, log, decode=False)

    file = open(play_queue.manege_cache(unload=False), "wb")
    file.write(s_bytes)
    path = file.name

    return path

