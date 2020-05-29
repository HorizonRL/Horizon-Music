import threading
import socket

from src.network import ServerManeger
from src.network.OperationType import OperationType
from src.utils.Logger import Logger
from src.utils.Constants import Network
from src.network.NetworkCommunication import *


class MultiServer:
    def __init__(self, logger):
        self.s_s = socket.socket()
        self.s_s.bind(('', Network().PORT))
        self.s_s.listen(20)

        self.clients = []
        self.log = logger

    def accept(self):
        sock, address = self.s_s.accept()

        t = threading.Thread(target=self.handle_client, args=(sock, address))
        self.clients.append(sock)
        t.start()

    def handle_client(self, sock, address):
        self.log.write("Client: {} CONNECTED".format(address))
        done = False
        while not done:
            try:
                req = split_req(recv_req(sock, log))
                if req[0] in OperationType.list():
                    ServerManeger.init(sock, self.log)
                    ServerManeger.do_req(req, address)

                else:
                    log.write("Invalid request by {}".format(address))
            except OSError:
                done = True
                sock.close()
                self.clients.remove(sock)
                continue


    def run(self):
        log.write("Starting Server!")
        while True:
            self.accept()


if __name__ == '__main__':
    log = Logger(log_name="Server")
    server = MultiServer(log)

    server.run()
    server.s_s.close()
