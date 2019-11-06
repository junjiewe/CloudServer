import socket #socket library

sock = socket.socket()

sock.bind(('127.0.0.1',5000)) #address to dock on home 
print('server started, listeining for clients...')

sock.listen(10) #upto five incoming request in the queue

con, addr = sock.accept() #start listeing, con is connection to send adn recv, addr is to store
print('Connection made at IP: ', str(addr[0]))

message = ("")
while message != 'wq':
    message = con.recv(1024).decode('utf-8')
    print(message)

print('Closing server and connection..')
con.close()
sock.close()
