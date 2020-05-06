import logging
from pathlib import Path


class Logger:
    def __init__(self, log_name='HorizonLog', is_console=True):
        self.log_name = log_name
        self.is_console = is_console

        self.logger = logging.getLogger(self.log_name)

        self.log = logging.FileHandler(str(Path.cwd() / 'logs' / str(self.log_name + '.log')).replace('src', ''))
        self.log.setLevel(logging.INFO)

        self.logger.addHandler(self.log)

    def log_error(self, msg):
        self.logger.error(msg)
        if self.is_console:
            print('\033[91m' + msg + '\033[0m')

    def log_to_console(self, msg):
        self.is_console = True
        print('\x1b[6;30;42m' + msg + '\x1b[0m')
