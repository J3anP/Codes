import socket
from threading import Thread
import time
import sys 

def leer_archivo():
    archivo = (open("PartesDeElectronica.csv", "r", encoding = "latin")).read()
    return archivo

def enviar_filas(s_client, archivo):
    filas = archivo.split("\n")
    for i in range(1,len(filas)):
        fila = filas[i]
        s_client.sendall(fila.encode())
        time.sleep(1)

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.18.9"; port = 5000
    s.bind((host,port))
    s.listen()
    print(f"Servidor escuchando en {host}: {port}")
    
    while True:
        sock_client, sock_add = s.accept()
        leer = Thread(target=leer_archivo, args=(sock_client,))
        enviar_fila = Thread(target = enviar_filas, args=(sock_client,leer_archivo()))
            
        leer.start()
        enviar_fila.start()
            
        leer.join()
        enviar_fila.join()
        
        sock_client.close()
   
        
        
        