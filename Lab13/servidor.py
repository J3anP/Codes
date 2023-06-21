import socket
from threading import Thread
import time
import sys
#import csv

def archivo_cliente(client_socket):
    archivo_thread = Thread(target = leer_archivo_cliente, args = (client_socket,))
    archivo_thread.start()
    archivo_thread.join()
    client_socket.close()
    
def leer_archivo_cliente(client_socket):
    with open("PartesDeElectronica.csv", "r") as archivo:
        #csv_reader = csv.reader(archivo)
        #aquí te quedaste solo falta eliminar la primera fila del archivo lo demás sale por sí solo
        filas = (archivo.read()).split("\n")
        for i in range(1,len(filas)):
            fila = filas[i]
            client_socket.sendall(fila.encode("utf-8"))
            time.sleep(1)
            
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 5001
    
    s.bind((host,port))
    s.listen()
    
    print(f"Servidor escuchando en {host}: {port}")
    try:
        while True:
            client_socket, address = s.accept()
            print(f"Conexión entrante desde {address[0]}:{address[1]}")
            
            #Hilo para manejar al cliente
            client_tread = Thread(target = archivo_cliente, args = (client_socket,))
            client_tread.start()
    except KeyboardInterrupt:
        sys.exit()
    except ConnectionResetError:
        sys.exit()
        
if __name__ == "__main__":
    main()
    
    