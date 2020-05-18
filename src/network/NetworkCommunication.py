
SEPARATOR_CHAR = "|||"
HEADER = 10


def assemble_req(*requests):
    final_req = ''
    for request in requests:
        final_req += "{}{}".format(request, SEPARATOR_CHAR)

    return final_req


def split_req(req):
    return req[:len(req) - len(SEPARATOR_CHAR)].split(SEPARATOR_CHAR)


def send_req(req, socket_, logger, encode=True):
    size = str(len(req)).zfill(HEADER)
    socket_.send(bytes(size.encode()))

    logger.write("Sending Request in size {} to {}".format(str(len(req)), socket_.getsockname()))
    socket_.send(req.encode() if encode else req)


def recv_req(socket_, logger, decode=True):
    size = int(str(socket_.recv(HEADER).decode()))
    req = socket_.recv(size + 1)

    logger.write("Receiving Request in size: {}".format(size))
    return req.decode() if decode else req
