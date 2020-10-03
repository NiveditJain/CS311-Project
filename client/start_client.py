import socket
import settings
import flags

ADDR = (settings.HOST, settings.PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(ADDR)
    message = flags.CREATE_OBJ
    client.send(message)

    message = "random music.mp3"
    message = message.encode('utf-8')
    client.send(message + b' ' * (settings.EXCHANGE_SIZE - len(message)))

    message = "Hello World.mp3"
    message = message.encode('utf-8')
    client.send(message + b' '*(settings.EXCHANGE_SIZE - len(message)))

    file = open('music\music.mp3', 'rb')
    data = file.read(settings.EXCHANGE_SIZE)

    while data:
        client.send(data)
        data = file.read(settings.EXCHANGE_SIZE)
