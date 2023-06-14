import socket
import sys

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('127.0.0.1',3000)
    s.bind(server_address)
    s.listen(1)
    print("Esperando conexiones...")
    
    try:
        conn, client_address = s.accept()
        print(f"Conexion entrante de: ('{client_address[0]}',{client_address[1]})")
        data = conn.recv(1024).decode()
        with open("oferta_del_sniper.txt","a+") as oferta:
            oferta.write(data)
        
    except KeyboardInterrupt:
        print("Cerrando el servidor...")
        sys.exit()
    finally:
        conn.close()
