import socket
import threading 


class Peer:
    def __init__(self, name, port):
        self.name = name
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def run(self):
        threading.Thread(target=self.server).start()
        threading.Thread(target=self.client).start()
    
    def server(self):
        self.socket.bind((socket.gethostname(), self.port))
        self.socket.listen()
        while True:
            client, addr = self.socket.accept()
            client.send(bytes(str(input(">")), 'utf-8'))
    def client(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((socket.gethostname(), 8080))
            msg = s.recv(1024)
            print(msg.decode("utf-8"))
            s.close()

peer = Peer('b', 8081)
peer.run()