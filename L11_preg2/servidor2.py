import socket


if __name__ == '__main__':
    sock_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock_s.bind(('0.0.0.0',5001))
    
    print("Buscando cliente")
    sock_s.listen(1)
    
    while True:
        try:
            conn, client_addr = sock_s.accept()
            print("Conectado")
            while True:
                sock_s.settimeout(0.1)
                contenido_nuevo = ""
                data = conn.recv(1024)
                if data: 
                    data = data.decode("utf-8")
                    data = data +"\n"
                    contenido_nuevo += f"{data}"
                    with open("pacientes.csv","r") as f:
                        contenido = f.read()
                    contenido += f"\n{contenido_nuevo}"
                    
                    with open("pacientes.csv", "w+") as f:
                        f.write(contenido)
                else:
                    print("No se ingresaron más datos")
                    break
    
        except ConnectionResetError:
            print("El cliente ha cerrado la conexión de manera abrupta")
        except KeyboardInterrupt:
            break
        finally:
            conn.close()