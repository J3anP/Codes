import socket
import time
import sys
if __name__ == '__main__':
    sock_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(f"Conectando a 172.0.0.1: 5001")
    
    sock_c.connect(("127.0.0.1",5001))
    datos = []
    try:
        print("Ingrese datos del paciente")
        Nombre = input("Nombre(s): ")
        Apellidos = input("Apellidos: ")
        Peso = input("Peso(kg): ")
        Talla = input("Talla(cm): ")
        Edad = input("Edad: ")
        Seguro = input("¿Cuenta con seguro? (s/n): ")
        if Seguro.lower=="s":
            Seguro = "True"
        if Seguro.lower=="n":
            Seguro = "False"
        
        datos = [Nombre, Apellidos, Peso, Talla, Edad, Seguro]
        
        msg = ",".join(datos)
        sock_c.sendall(msg.encode("utf-8"))
        
        time.sleep(1)
        print("Enviando al servidor...")
    except KeyboardInterrupt:
        sys.exit()  
    
