
SEPARATOR_CHAR = "|||"
BUFFER_SIZE = 16


def assemble_req(*requests):
    final_req = ''
    for request in requests:
        final_req += "{}{}".format(request, SEPARATOR_CHAR)

    return "{}{}{}".format(len(final_req), SEPARATOR_CHAR, final_req)


def split_req(req):
    return req[:len(req) - len(SEPARATOR_CHAR)].split(SEPARATOR_CHAR)


def send_req(req, socket_, logger):
    logger.write("sending request {} to {}".format(req, socket_.getsockname()))
    socket_.send(req.encode())


def send_file(file, socket_, logger):
    logger.write("sending file")
    socket_.sendall(file)


def recv_req(socket_, logger):
    data = socket_.recv(BUFFER_SIZE).decode()
    length = None
    req = None
    is_length_done = False

    while not is_length_done:
        data += socket_.recv(BUFFER_SIZE).decode()
        if data.find(SEPARATOR_CHAR) is not -1:
            sep = data.find(SEPARATOR_CHAR)
            length = data[:sep]
            req = data[sep:]
            is_length_done = True

    while len(req) <= int(length):
        req += socket_.recv(BUFFER_SIZE).decode()

    req = req[len(SEPARATOR_CHAR):]
    logger.write("receiving request {}".format(req))
    return req
