import runchecks
import setup
import socket
import settings
import request_handler
import threading

print('Identifying IP!')
HOST = socket.gethostbyname(socket.gethostname())
print('Your IPv4, is ' + str(HOST))

ADDR = (HOST, settings.PORT)
print('Starting Server on {}:{}'.format(HOST, settings.PORT))

# starting TCP protocol over IPv4
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    try:
        server.bind(ADDR)
        server.listen()

        print('server successfully started at {}:{}!'.format(HOST, settings.PORT))
        print('Please disallow for Private Network Firewall (will be prompted), ignore is already disallowed!')

    except:
        raise Exception(
            'could not start server, this could be some issue with your proxy settings or firewall settings or some other app is using this PORT!')

    # making server running continuously
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=request_handler.gate_way, args=(connection, address))
        print('Starting Connection with {}'.format(address))
        thread.start()
        print('active connections = {}'.format(threading.activeCount() - 1))