import socket

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
    horizon_music = HorizonMusic(log)

    params = Network()

    try:
        client.connect((params.SERVER_IP, params.PORT))

    except ConnectionRefusedError as err:
        log.write("Connection timeout! - You are using Horizon Music offline |{}".format(err))

    finally:
        horizon_music.app.run()
        log.write("{} EXIT\n".format(socket.gethostname()))
