import socket

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
    horizon_music = HorizonMusic(log)

    params = Network()
    is_online = True

    try:
        client.connect((params.SERVER_IP, params.PORT))

    except ConnectionRefusedError as err:
        log.write("Connection timeout! - You are using Horizon Music offline |{}".format(err))
        is_online = False

    finally:
        horizon_music.app.run()
        if is_online:
            send_req(assemble_req(OperationType.DISCONNECT.name), client, log)
