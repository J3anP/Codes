import socket
import pickle
import numpy as np

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1",5000)
    print(f"Iniciando servidor en IP {server_address[0]}, con puerto {server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)

    sock.settimeout(1)
    try:
        print("Esperando conexiones...")
        while True:
            try:
                conn, addr = sock.accept()
                print(f"Conexión desde {addr[0]}:{addr[1]}")
                imagen = pickle.loads(conn.recv(4248))
                # for i in range(64):
                #     for j in range(64):
                #         imagen[i][j] = 255 - imagen[i][j]
                imagen_negativa = 255-imagen
                conn.sendall(pickle.dumps(imagen_negativa))
                conn.close()
                print("Cerrando conexión con el cliente")
                print("Esperando conexiones...")
            except TimeoutError:
                pass
    except KeyboardInterrupt:
        print("Cerrando servidor")
        sock.close()
