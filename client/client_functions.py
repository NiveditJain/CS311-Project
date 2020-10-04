import socket
import flags
import settings
import utils
import os
import pickle

ADDR = (settings.HOST, settings.PORT)


def playlist_add(name, filename):
    if not utils.verify_file(filename):
        return False

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # connecting client to server
        client.connect(ADDR)

        # will sending operation flag
        client.send(flags.CREATE_OBJ)

        # sending name
        client.send(utils.padded_message(name.encode('utf-8')))

        # sending file name
        client.send(utils.padded_message(os.path.basename(filename).encode('utf-8')))

        # sending file
        file = open(filename, 'rb')
        data = file.read(settings.EXCHANGE_SIZE)

        while data:
            client.send(data)
            data = file.read(settings.EXCHANGE_SIZE)

    return True


def get_playlist():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(ADDR)
        client.send(flags.GET_LIST)

        size = int(client.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip())
        data = client.recv(size)
        data = pickle.loads(data)
    return data