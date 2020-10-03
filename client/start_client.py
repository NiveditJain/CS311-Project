import socket
import settings
import flags

ADDR = (settings.HOST, settings.PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(ADDR)
    message = flags.DISCONNECT
    client.send(message)