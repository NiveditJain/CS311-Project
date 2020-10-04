import flags
import settings
import time
import music
from playsound import playsound
import threading
import os
import pickle


def start_music_player():
    while True:
        music_obj = music.playlist.get_next()
        if music_obj is not None:
            path = os.path.join(settings.STORAGE, music_obj.filename)
            print(f'Playing... {music_obj.name} from {path}')
            playsound(path)
            music.playlist.clean_music()


thread = threading.Thread(target=start_music_player)
thread.start()


def object_create(connection, address):
    print(f'started object creation from {address}')

    name = connection.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip()
    print(f'{name} received from {address}')

    file_name = connection.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip()
    print(f'file name received {file_name} from {address}')

    file_name = file_name.split('.')[0]+'_'+str(int(time.time())%10000)+'.'+file_name.split('.')[1]
    music_file = open(os.path.join(settings.STORAGE, file_name), "wb")
    print(f'file ({file_name}) download started from {address}')

    data = connection.recv(settings.EXCHANGE_SIZE)
    while data:
        music_file.write(data)
        data = connection.recv(settings.EXCHANGE_SIZE)
    print(f'file ({file_name}) created success from {address}')

    music_obj = music.Music(file_name, name)
    music.playlist.add_music(music_obj)
    print(f'music object with id: {music_obj.id} created success from {address}')


# type = 1 for upvote
# type = -1 for downvote
def handle_votes(connection, address, upvote):

    id = int(connection.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip())
    vote = music.Vote(upvote)

    for music_obj in music.playlist.music_objs:
        if music_obj.id == id:
            music_obj.add_vote(vote)
    print(f'created vote object for request from {address}')


def send_list(connection, address):
    print(f'starting object list sending to {address}')
    my_list = []

    for music_objs in music.playlist.music_objs:
        my_list.append([music_objs.name, music_objs.id, music_objs.get_value()])

    data = pickle.dumps(my_list)

    size = str(len(data))
    print(f'byte size for list calculated {size} to send to {address}')
    size = size.encode('utf-8')
    size = size + b' ' * (settings.EXCHANGE_SIZE - len(size))
    connection.send(size)
    connection.send(data)


def send_file(connection, address):
    pass


def send_playing(connection, address):

    if music.playlist.playing is None:
        data = flags.NONE

    else:
        data = music.playlist.playing.name.encode('utf-8')

    print(f'sending playing name to {address}')
    size = str(len(data)).encode('utf-8')
    size = size + b' ' * (settings.EXCHANGE_SIZE - len(size))
    connection.send(size)
    connection.send(data)


def gate_way(connection, address):
    flag = connection.recv(flags.SIZE)
    print(f'from {address} [FLAG] {flag.decode("utf-8")}')

    if flag == flags.CREATE_OBJ:
        object_create(connection, address)

    elif flag == flags.GET_LIST:
        send_list(connection, address)

    elif flag == flags.CREATE_UPVOTE:
        handle_votes(connection, address, True)

    elif flag == flags.CREATE_DOWNVOTE:
        handle_votes(connection, address, False)

    elif flag == flags.LISTEN:
        send_file(connection, address)

    elif flag == flags.PLAYING:
        send_playing(connection, address)

    elif flag == flags.DISCONNECT:
        pass

    connection.close()
