import logging
from pathlib import Path

class Logger:
    def __init__(self, log_name='HorizonLog'):
        self.logger = logging.getLogger(log_name)

        log = logging.FileHandler(str(Path.cwd() / 'logs' / str(log_name + '.log')).replace('src', ''))
        log.setLevel(logging.INFO)

        self.logger.addHandler(log)

    def log_error(self, msg):
        self.logger.critical(msg)
        print('\033[91m' + msg + '\033[0m')

    def log_msg(self, msg):
        self.logger.info(msg)
        print('\x1b[6;30;42m' + msg + '\x1b[0m')


