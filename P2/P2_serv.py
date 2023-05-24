import socket
import pickle as plk
import numpy as np
SOCK_BUFFER = 1024

if __name__== '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('0.0.0.0',8000)
    sock.bind(server_address)
    sock.listen()
    print("Esperando conexiones...")
    while True:
        try:
            conn, client_address = sock.accept()
            print(f"Conexion entrante de: ('{client_address[0]}',{client_address[1]})")
            while True:
                data = conn.recv(SOCK_BUFFER)
                if data: 
                    matrices = plk.loads(data)
                    A = matrices[0]
                    B = matrices[1]
                    matriz_prod = np.dot(np.array(A),np.array(B))
                    C = matriz_prod.tolist()
                    conn.sendall(plk.dumps(C))
                else:
                    break
        except ConnectionResetError:
            print("Conexión cerrada por el cliente")
        finally:
            conn.close()
        sock.close()