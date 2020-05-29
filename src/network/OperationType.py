from src.utils.Enum import Enum


class OperationType(Enum):
    DISCONNECT = "DISCONNECT"
    REQ_SONG = "REQ_SONG"
    ALL_SONGS = "ALL_SONGS"
    DOWNLOAD = "DOWNLOAD"
