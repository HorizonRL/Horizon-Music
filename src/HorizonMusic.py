import socket
import threading

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
        log.write("Connection timeout! - You are using Horizon Music offline | {}".format(err))
        is_online = False

    finally:
        if is_online:  # Get music lib
            ClientDoReqs.init(client, log)
            ClientDoReqs.get_all_server_songs()

        horizon_music = HorizonMusic(log)
        app_thread = threading.Thread(target=horizon_music.app.run())
        app_thread.start()

        if is_online:
            ClientDoReqs.disconnect()
