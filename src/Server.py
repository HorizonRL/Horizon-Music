import threading
import socket

from src.utils.Logger import Logger
from src.utils.Constants import Network


class MultiServer:
    def __init__(self, logger):
        self.s_s = socket.socket()
        self.s_s.bind(('', Network().PORT))
        self.s_s.listen(1)

        self.clients = []
        self.log = logger

    def accept(self):
        sock, address = self.s_s.accept()
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
