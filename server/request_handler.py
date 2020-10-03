import socket
import flags


def gate_way(connection, address):
    flag = connection.recv(flags.SIZE)
    print('from {} [FLAG] {}'.format(address, flag.decode('utf-8')))



    if flag == flags.DISCONNECT:
        pass

    connection.close()