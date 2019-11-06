import socket

sock = socket.socket()

print('Connecting to the server')
sock.connect(('127.0.0.1',5000)) #connect to server

print('Conneted to server')
message = ''
while message != 'wq':
    message = str(input('>>> '))
    sock.send(message.encode('utf-8'))

print('Connection closed')


