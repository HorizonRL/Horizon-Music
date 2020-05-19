import threading
import socket

from src.network import ServerDoReqs
from src.network.OperationType import OperationType
from src.utils.Logger import Logger
from src.utils.Constants import Network
from src.network.NetworkCommunication import *


class MultiServer:
    def __init__(self, logger):
        self.s_s = socket.socket()
        self.s_s.bind(('', Network().PORT))
        self.s_s.listen(1690)

        self.clients = []
        self.log = logger

    def accept(self):
        sock, address = self.s_s.accept()

        t = threading.Thread(target=self.handle_client, args=(sock, address))

        self.clients.append(t)

        t.start()

    def handle_client(self, sock, address):
        self.log.write("Client: {} CONNECTED".format(address))
        while True:
            req = split_req(recv_req(sock, log))
            if req[0] in OperationType.list():
                ServerDoReqs.init(sock, self.log)
                ServerDoReqs.do_req(req, address)

            else:
                log.write("Invalid request by {}".format(address))

    def run(self):
        log.write("Starting Server!")
        while True:
            self.accept()


if __name__ == '__main__':
    log = Logger(log_name="Server")
    server = MultiServer(log)

    server.run()
    server.s_s.close()
