import socket
import time
from colorama import Fore, init
SOCK_BUFFER = 1024 

if __name__ =='__main__':
    init()
    while True:
        
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            server_address = ("192.168.72.1",3000)
            sock.connect(server_address)
            print(Fore.GREEN+"[*] El servidor está operativo")
        except ConnectionError:
            print(Fore.RED+"[-] El servidor no responde")
        finally:
            sock.close()
            time.sleep(5)