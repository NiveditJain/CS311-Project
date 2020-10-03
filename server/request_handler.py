import socket
import flags
import settings
import time
import os
import music

def object_create(connection, address):
    print(f'started object creation from {address}')

    name = connection.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip()
    print(f'{name} received from {address}')

    file_name = connection.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip()
    print(f'file name received {file_name} from {address}')

    music_file = open(os.path.join(settings.STORAGE, file_name.split('.')[0]+'_'+str(int(time.time())%10000)+'.'+file_name.split('.')[1]), "wb")
    print(f'file ({file_name}) download started from {address}')

    data = connection.recv(settings.EXCHANGE_SIZE)
    while data:
        music_file.write(data)
        data = connection.recv(settings.EXCHANGE_SIZE)
    print(f'file ({file_name}) created success from {address}')

    music_obj = music.Music(file_name, name)
    music.playlist.add_music(music_obj)
    print(f'music object with id: {music_obj.id} created success from {address}')


def gate_way(connection, address):
    flag = connection.recv(flags.SIZE)
    print(f'from {address} [FLAG] {flag.decode("utf-8")}')

    if flag == flags.CREATE_OBJ:
        object_create(connection, address)

    elif flag == flags.DISCONNECT:
        pass

    connection.close()