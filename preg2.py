import socket,pickle
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    try:
        puerto=np.random.randint(1000,5001)
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Inicializando servicio en el puerto {puerto}...")
        sock.bind(("localhost",puerto))
        sock.listen(1)
        while True:
            sock.settimeout(0.1)
            while True:
                try:
                    conn,clientAddress=sock.accept()
                    break
                except TimeoutError:
                    pass
            sock.settimeout(None)
            print(f"¡Conexión exitosa con {clientAddress}!")
            while True:
                try:
                    conn.sendall(pickle.dumps(255*np.ones((64,64),dtype=np.uint8)-pickle.loads(conn.recv(4248))))
                except EOFError:
                    conn.close()
                    print("Conexión perdida :(\nAceptando nuevas conexiones...")
                    break
    except KeyboardInterrupt:
        print("Finalizando programa...")