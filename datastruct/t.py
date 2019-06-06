import socket
import sys

def start_tcp_sever(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sever_address = (host, port)
    sock.bind(sever_address)

    try:
        sock.listen(5)
    except socket.error:
        sys.exit(1)

    while True:
        print("waiting for connection")

        conn, addr = sock.accept()
        buf = conn.recv(1024)
        print(buf)

        conn.send('shoudao')
        conn.close()



class Stack:
    def __init__(self):
        self.__items = []
    def isempty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.__items)
    def peek(self):
        assert not self.isempty()
        return self.__items[-1]

    def push(self, value):
        self.__items.append(value)

    def pop(self):
        assert not self.isempty()
        return self.__items.pop()


