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

        print(f'server successfully started at {HOST}:{settings.PORT}!')
        print('Please disallow for Private Network Firewall (will be prompted), ignore if already disallowed!')

    except:
        raise Exception(
            'could not start server, this could be some issue with your proxy'
            'settings or firewall settings or some other app is using this PORT!')

    # making server running continuously
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=request_handler.gate_way, args=(connection, address))
        print(f'Starting Connection with {address}')
        thread.start()
        print(f'active connections = {threading.activeCount() - 2}')