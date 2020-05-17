import logging
from pathlib import Path
from datetime import datetime
import os


class Logger:
    def __init__(self, log_name='HorizonLog', is_console=True):
        self.log_name = log_name
        self.is_console = is_console

        self.logger = logging.getLogger(self.log_name)

        path = os.path.join(str(Path.cwd()).replace('src', ''), 'logs')

        try:
            os.makedirs(path)

        except FileExistsError:
            pass

        self.log = logging.FileHandler(os.path.join(path, self.log_name + '.log'))
        self.log.setLevel(logging.INFO)

        self.logger.addHandler(self.log)

    def write(self, msg):
        self.logger.error("{} --> {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), msg))
        if self.is_console:
            print("[LOG]\033[1;36m {} \033[;1m".format(msg))
