import socket
import time
import sys
if __name__ == '__main__':
    sock_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(f"Conectando a 172.0.0.1: 5001")
    
    sock_c.connect(("192.168.72.1",5001))
    datos = []
    try:
        print("Ingrese datos del paciente")
        Nombre = input("Nombre(s): ")
        time.sleep(0.1)
        Apellidos = input("Apellidos: ")
        time.sleep(0.1)
        Peso = input("Peso(kg): ")
        time.sleep(0.1)
        Talla = input("Talla(cm): ")
        time.sleep(0.1)
        Edad = input("Edad: ")
        time.sleep(0.1)
        Seguro = input("¿Cuenta con seguro? (s/n): ")
        if Seguro.lower == "s":
            Seguro = "True"
        else:
            Seguro = "False"
        time.sleep(0.1)
        
        datos = [Nombre, Apellidos, Peso, Talla, Edad, Seguro]
        
        msg = ",".join(datos)
        sock_c.sendall(msg.encode("utf-8"))
        
        time.sleep(2)
        print("Enviando al servidor...")
    except KeyboardInterrupt:
        sys.close()  
    finally:
        sock_c.close()