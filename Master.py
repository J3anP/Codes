import socket
import time

if __name__ == '__main__':
    sM = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sM.bind(("127.0.0.1",5002))
    sM.listen()
    
    while True:
        try:
            conn, serv1_add = sM.accept()
            print(f"Conexión desde: {serv1_add[0]}: {serv1_add[1]}")
            
            while True:
                with open("pregunta1.txt") as song:
                    for linea in song:
                        conn.sendall(linea.encode("utf-8"))
                        
                        time.sleep(1)
                        
                    #song.close()
        except KeyboardInterrupt:
            break 
        except ConnectionResetError:
            print("El servidor ha cerrado la sesión de manera abrupta")
        except ConnectionAbortedError:
            print("El servidor ha anulado la conexión")
