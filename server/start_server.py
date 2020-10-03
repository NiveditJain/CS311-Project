import runchecks
import setup
import socket
import settings

print('Identifying IP!')
HOST = socket.gethostbyname(socket.gethostname())
print('Your IPv4, is ' + str(HOST))

ADDR = (HOST, settings.PORT)
print('Starting Server on {}:{}'.format(HOST, settings.PORT))