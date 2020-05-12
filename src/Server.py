import threading
import socket

from src.utils.Logger import Logger
from src.utils.Constants import Network


class MultiServer:
    def __init__(self, logger):
        self.ss = socket.socket()
        self.ss.bind(('', Network().PORT))
        self.ss.listen(1)

        self.clients = []
        self.log = logger

    def accept(self):
        sock, address = self.ss.accept()
        self.clients += [threading.Thread(target=self.handle_client, args=(sock, address)).start()]

    def handle_client(self, sock, address):
        self.log.write("Client:{} CONNECTED".format(address))

    def run(self):
        self.log.write("Server starting")
        while True:
            self.accept()


if __name__ == '__main__':
    log = Logger(log_name="Server")
    server = MultiServer(log)
    server.run()
