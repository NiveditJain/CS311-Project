import socket
import settings
import flags
import pickle

ADDR = (settings.HOST, settings.PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(ADDR)
    message = flags.GET_LIST
    client.send(message)

    size = int(client.recv(settings.EXCHANGE_SIZE).decode('utf-8').strip())
    data = client.recv(size)
    data = pickle.loads(data)
    print(data)
