import socket

SOCK_BUFFER = 1024 

if __name__ =='__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.72.1",5000)
    
    print("Conectado a servidor.")
    try: 
        sock.connect(server_address)
        turn = False
        while True:
            if turn:
                mensaje_enviar = input(">")
                    
                if mensaje_enviar.lower() == "salir":
                    sock.sendall(mensaje_enviar.encode())
                    break   
                else:
                    sock.sendall(mensaje_enviar.encode())
                    turn = False
            else:
                data = sock.recv(SOCK_BUFFER)
                mensaje_recv = data.decode()
                if mensaje_recv.lower() == "salir":
                    break
                print(f"Recibido: {data.decode()}")
                turn = True
    except ConnectionResetError:
        print("El servidor cerró la conexión de manera abrupta")
    except KeyboardInterrupt:
        mensaje_enviar = "salir"
        sock.sendall(mensaje_enviar.encode())
    finally:
        sock.close()
        