import socket
import sys
import time 

if __name__ == "__main__":

    sock_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock_c.connect(("127.0.0.1",5000))
        while True:
            data = sock_c.recv(1024)
            cant_bytes = data.decode()
            print(f"HOLA SOY CLIENTE Y LA CANTIDAD DE CARACTERES RECIBIDA POR SERVIDOR ES {cant_bytes}")
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()
    finally:
        sock_c.close()
