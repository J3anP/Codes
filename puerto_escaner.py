import socket
import sys
from datetime import datetime

if __name__ == '__main__':
    
    
    if len(sys.argv) == 2:
        IP = socket.gethostbyname(sys.argv[1])
    else:
        print("Ingrese los datos correctamente")
        exit()
    
    try :
        for port in range(1,100):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #tiempo de espera para conexión de cliente
            
            socket.setdefaulttimeout(1)
            
            result = sock.connect_ex((IP, port))
            
            if result == 0:
                print(f"Puerto {port} está abierto")
            sock.close()
    except KeyboardInterrupt:
        sys.exit()
    except socket.gaierror:
        print("El nombre del host no es válido")
        sys.exit()
    except socket.error:
        print("Host no responde")
        sys.exit()    
    finally:
        print("Fin del programa")
