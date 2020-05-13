import enum

SEPARATOR_CHAR = "|||"


def assemble_req(*requests):
    final_req = ''
    for request in requests:
        final_req += "{}{}".format(request, SEPARATOR_CHAR)

    return final_req


def split_req(req):
    return req[:len(req) - len(SEPARATOR_CHAR)].split(SEPARATOR_CHAR)


class ClientRequests(enum.Enum):
    DISCONNECT = "DISCONNECT"
    CONNECT = "CONNECT"
    REQ_SONG = "REQ_SONG"
    SEARCH = "SEARCH"
    ALL_SONGS = "ALL_SONGS"
    DOWNLOAD = "DOWNLOAD"


class ServerRequests(enum.Enum):
    CONNECT = "CONNECT"
    SEND_SONG = "SEND_SONG"
    SEARCH = "SEARCH"
    ALL_SONGS = "ALL_SONGS"
    DOWNLOAD = "DOWNLOAD"
