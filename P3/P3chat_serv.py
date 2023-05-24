import socket

SOCK_BUFFER = 1024 

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('0.0.0.0',5000)
    
    sock.bind(server_address)
    sock.listen()
    
    while True:
        try:
            print("Server started and listening on port 5000")
            conn,client_add = sock.accept()
            print(f"Conectando al cliente: ('{client_add[0]}',{client_add[1]})")
            turn = True
            
            while True:
                if turn:
                    message = input(">")
                    
                    if message.lower() == 'salir':
                        conn.sendall(message.encode())
                        break
                    else:
                        conn.sendall(message.encode())
                        turn = False
                else:
                    data = conn.recv(SOCK_BUFFER)
                    message_recv = data.decode()
                    if message_recv.lower() =='salir':
                        break
                    print(f"Recibido: {data.decode()}")
                    turn = True
        
        except ConnectionResetError:
            print("El cliente cerró la conexión de manera abrupta")
        except KeyboardInterrupt:
            message = 'salir'
            conn.sendall(message.encode())
        finally:
            conn.close()
            break
    sock.close()        
  
                
        
    