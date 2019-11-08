import socket #socket library
from handleMultiple import clientHandler

sock = socket.socket()

sock.bind(('127.0.0.1',5000)) #address to dock on home 
print('server started, listeining for clients...')

sock.listen(10) #upto ten incoming request in the queue

while True:
    con, addr = sock.accept() #start listeing, con is connection to send adn recv, addr is to store
    print('Connection made at IP: ', str(addr[0]))
    print('Passing off client..')
    client = clientHandler(con, addr[0])
    client.start()

print('Closing server and connection..')
con.close()
sock.close()
