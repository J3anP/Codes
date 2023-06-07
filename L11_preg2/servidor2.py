import socket
import time

if __name__ == '__main__':
    sock_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock_s.bind(('127.0.0.1',5001))
    
    print("Buscando cliente")
    sock_s.listen(1)
    
    while True:
        time.sleep(0.5)
        conn, client_addr = sock_s.accept()
        print("Conectado")
        try:
            
            while True:
                contenido_nuevo = ""
                data = conn.recv(1024)
                if data: 
                    data = data.decode("utf-8")
                    contenido_nuevo += f"{data}"
                    with open("pacientes.csv","r") as f:
                        contenido = f.read()
                    contenido += f"\n{contenido_nuevo}"
                    
                    with open("pacientes.csv", "w+") as f:
                        f.write(contenido)
                        
                    print("Guardando datos")
                
        except ConnectionResetError:
            print("El cliente ha cerrado la conexión de manera abrupta")
        except KeyboardInterrupt:
            break
        finally:
            conn.close()
    sock_s.close()
