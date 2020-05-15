import socket

from src.network import ClientDoReqs
from src.network.OperationType import OperationType
from src.ui.UIHandler import HorizonMusicApp
from src.utils.Logger import Logger
from src.utils.Constants import Network
from src.network.NetworkCommunication import *


class HorizonMusic:
    def __init__(self, logger):
        self.logger = logger
        self.app = HorizonMusicApp(self.logger)


if __name__ == "__main__":
    client = socket.socket()
    log = Logger(log_name="{}-log".format(str(socket.gethostname())))

    params = Network()
    is_online = True

    try:
        client.connect((params.SERVER_IP, params.PORT))

    except ConnectionRefusedError as err:
        log.write("Connection timeout! - You are using Horizon Music offline |{}".format(err))
        is_online = False

    finally:
        if is_online:  # Get music lib
            send_req(assemble_req(OperationType.ALL_SONGS.name), client, log)
            ClientDoReqs.get_all_server_songs(recv_req(client, log))

        horizon_music = HorizonMusic(log)
        horizon_music.app.run()
        if is_online:
            send_req(assemble_req(OperationType.DISCONNECT.name), client, log)
