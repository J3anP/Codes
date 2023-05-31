import random as rd
import socket
import sys 

my_IP = "127.0.0.1"
port = 5000

#Diccionario de donde se escoge palabras al azar para el juego
dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]

def descubrirpista(palabra_rd, letra, palabraClient):
    palrd_new = palabra_rd
    letraClient = letra
    
    pista = '*'*len(palabra_rd)
    for i in range(len(palrd_new)):
        if palrd_new[i] == letraClient:
            nPri = pista[:i] 
            nUlt = pista[i+1:]
            pista = nPri + letraClient + nUlt
    #return pista
            
    #for i in range(len(palrd_new)):
        #if palrd_new[i] == letraClient:
            #nPri = len(palabra_rd[:i])
            #nUlt = len(palabra_rd[i+1:])
            #pista = nPri*'*'+letraClient+nUlt*'*'
    #return pista
    
    #for letraClient in palrd_new:
        #if letraClient in palabraClient:
            #return (letraClient,end="")
        #else:
            #return ("*",end="")

    

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock.bind((my_IP, port))
    
    sock.listen()
    
    print(f"Arrancando servidor en {my_IP}:{port}")
    print("Esperando una nueva conexión de un cliente")
    conn,cliente_add = sock.accept()
    
    print(f"...conexión de: ('{cliente_add[0]}', {cliente_add[1]})")
    

    try:
        #comando = conn.recv(1024).decode()
        #if comando == 'start':
            #print(f"Recibí comando: {comando}")
            #pass
        errores = 0            
        palabra = rd.choice(dictionary)
        print(f"Palabra elegida: {palabra}")
        
        while errores>5:
            
            #comando = conn.recv(1024).decode()
            #letraClient = comando
            letraClient = conn.recv(1024).decode()
            print(f"Client guess: {letraClient}")
            
            descubierto = descubrirpista(palabra, letraClient)
                
            conn.sendall(descubierto.encode())
                
            if letraClient not in palabra:
                errores += 1
                        
            if descubierto == palabra:
                conn.sock.sendall("Ganaste".encode())
                break
                        
        if descubierto!= palabra:
                conn.sendall("Perdiste".encode())  
                             
    except KeyboardInterrupt:
        sys.exit()
    except socket.error:
        print("No hay respuesta del cliente".encode())
        sys.exit()
    finally:
        conn.close()
    sock.close()