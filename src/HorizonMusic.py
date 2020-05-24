import socket
import threading

from src.network import ClientManeger
from src.ui.UIHandler import HorizonMusicApp
from src.utils.Logger import Logger
from src.utils.Constants import Network


class HorizonMusic:
    def __init__(self, logger):
        self.logger = logger
        self.app = HorizonMusicApp(self.logger)


if __name__ == "__main__":
    client = socket.socket()
    log = Logger(log_name="{}-log".format(str(socket.gethostname())))

    params = Network()

    try:
        client.connect((params.SERVER_IP, params.PORT))

    except ConnectionRefusedError as err:
        log.write("Connection timeout! - You are using Horizon Music offline | {}".format(err))
        params.IS_ONLINE = False

    finally:
        ClientManeger.init(client, log, params.IS_ONLINE)
        if params.IS_ONLINE:  # Get music lib
            ClientManeger.get_all_server_songs()

        horizon_music = HorizonMusic(log)
        app_thread = threading.Thread(target=horizon_music.app.run())
        app_thread.start()
        log.write("App Starting!")

        if params.IS_ONLINE:
            ClientManeger.disconnect()
