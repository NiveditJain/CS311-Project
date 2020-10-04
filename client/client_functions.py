import socket
import flags
import settings
import utils
import os
import pickle
from playsound import playsound

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

        file.close()

    return True


def get_playlist():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(ADDR)
        client.send(flags.GET_LIST)

        size = int(client.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip())
        data = client.recv(size)
        data = pickle.loads(data)
    return data


def get_playing():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(ADDR)
        client.send(flags.PLAYING)

        size = int(client.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip())
        data = client.recv(size)

        if data == flags.NONE:
            return None

        return data.decode('utf-8')


def create_upvote(id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(ADDR)
        client.send(flags.CREATE_UPVOTE)

        client.send(utils.padded_message(str(id).encode('utf-8')))


def create_downvote(id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(ADDR)
        client.send(flags.CREATE_DOWNVOTE)

        client.send(utils.padded_message(str(id).encode('utf-8')))


def listen(id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(ADDR)
        client.send(flags.LISTEN)

        client.send(utils.padded_message(str(id).encode('utf-8')))

        flag = client.recv(flags.SIZE)

        if flag == flags.NONE:
            print('no music found at this ID')
            return

        elif flag == flags.SUCCSESS:
            filename = client.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip()

            filename = os.path.join('temp',filename)
            music_file = open(filename, 'wb')

            data = client.recv(settings.EXCHANGE_SIZE)
            while data:
                music_file.write(data)
                data = client.recv(settings.EXCHANGE_SIZE)
            music_file.close()

            playsound(filename)
            os.remove(filename)
