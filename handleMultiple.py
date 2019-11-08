import threading
import sys

class clientHandler(threading.Thread):
    def __init__(self, con, IP):
        self.con = con
        self.IP = IP

        super(clientHandler, self).__init__() #set up and start the thread
    
    def run(self):
        message = ''
        while message != 'wq':
            message = self.recvData()
            print(message)
        
        print('Closing Clients Connection with: ', self.IP)

    def recvData(self):
        message = self.con.recv(1024)
        return message.decode('utf-8')

    def recvByteData(self):
        message = self.con.recv(1024)
        return message   

    def sendData(self,data):
        try:    #Use try and execpt to prevent program exit when error happens
            data = data.encode('utf-8')
            self.con.send(data)
            return True #will try a couple times if fails sending
        except:
            print('Error', str(sys.exc_info()[0])) #return the last error if something went wrong
            return False