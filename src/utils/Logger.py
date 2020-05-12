import logging
from pathlib import Path
from datetime import datetime


class Logger:
    def __init__(self, log_name='HorizonLog', is_console=True):
        self.log_name = log_name
        self.is_console = is_console

        self.logger = logging.getLogger(self.log_name)

        self.log = logging.FileHandler(str(Path.cwd() / 'logs' / str(self.log_name + '.log')).replace('src', ''))
        self.log.setLevel(logging.INFO)

        self.logger.addHandler(self.log)

    def write(self, msg):
        self.logger.error("{} | {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), msg))
        if self.is_console:
            print('\x1b[6;30;42m' + msg + '\x1b[0m')
