import socket
from sys import getsizeof
import time

if __name__ == '__main__':
    s_M= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_C = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_C.bind(("127.0.0.1",5000))
    s_C.listen()
    print("Conectando al servidor Maestro...")
    while True:
        try:
            conn,client1 = s_C.accept() #acepta conexión de cliente1
            
            s_M.connect(("127.0.0.1",5002))
            while True: 
                data = s_M.recv(1024).decode('utf-8')
                tamanio = f":{getsizeof(data)}"
                print(f"HOLA SOY SERVIDOR Y HE RECIBIDO DE MASTER {tamanio} bytes: ")
                print(f"{data}")
                
                
                if conn:
                    conn.sendall(tamanio.encode()) #enviando cantidad de bytes a cliente1
                    time.sleep(0.01)
                else:
                    s_C.close()
    
        except KeyboardInterrupt:
            break
        except ConnectionAbortedError:
            pass
        #finally:
            #s_M.close()
