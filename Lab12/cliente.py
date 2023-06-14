import socket 

if __name__ == '__main__':
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1",3000))
    
    puja = input()
    sock.sendall(puja.encode())
    
    sock.close()