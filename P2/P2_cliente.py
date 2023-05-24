import socket
import pickle as plk
import numpy as np


SOCK_BUFFER = 1024 

if __name__ =='__main__':
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = ("192.168.72.1",8000)
    sock.connect(server_address)
    
    A = [[1,2],[3,4]]
    B = [[1,0],[0,1]]

    try:
        data=[A,B]
        print(A)
        print(B)
        sock.sendall(plk.dumps(data))
        matrizP = sock.recv(SOCK_BUFFER)
        C = plk.loads(matrizP)
        print(f"El producto de matrices:\n{C}")
    finally:
        sock.close()