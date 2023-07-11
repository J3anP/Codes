import socket
from threading import Thread 

def recibir_datos(sock):
    global bandera 
    bandera = None
    while True:
        fila = sock.recv(1024).decode()
        if fila:
            filas.append(fila)
            bandera = True
        else:
            bandera = False
            break

def procesar():
    i = 0
    #costo_neto = 0
    cont_el = 0
    cont_peso = 0
    cont_bajo = 0
    while True:
        if bandera == True:
            cabecera = filas[i].split(";")
            
            nombre = cabecera[1]
            cantidad = int(cabecera[3])
            peso = float(cabecera[4])
            unit_cost = float(cabecera[5])
            costo_componente = calcular_costo_componente(cantidad,unit_cost)
            #costo_neto += costo_componente
            clasificacion = clasificacion_componente(costo_componente)
            
            print(f"----------------Nombre:{nombre}----------------")
            print(f"Costo total: {costo_componente}")
            print(f"Clasificación por costo: {clasificacion}")
            
            if costo_componente>75:
                cont_el += cantidad
                if peso>100:
                    cont_peso += cantidad
                                
            if costo_componente <25:
                cont_bajo += cantidad
            print(f"Número de componentes con costo elevado: {cont_el}")
            print(f"Número de componentes con costo elevado y peso mayor a 100g: {cont_peso}")
            print(f"Número de componentes con costo bajo: {cont_bajo}")                  
            i+=1
        else:
            if bandera == False:
                break
            
def calcular_costo_componente(cant,cost_u):
    return cant*cost_u         

def clasificacion_componente(costo_c):
    if costo_c < 25:
        return "Costo bajo"
    elif(costo_c<50):
        return "Costo regular"
    elif(costo_c<75):
        return "Costo alto"
    else:
        return "Costo elevado"        
            
        
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            sock.connect(("192.168.18.9",5000))
        except KeyboardInterrupt:
            break
        
    filas = []
    lectura = Thread(target= recibir_datos, args = (sock,))
    procesar_datos = Thread(target = procesar, args = ())
    lectura.start()
    procesar_datos.start()
    lectura.join()
    procesar_datos.join()
    
    sock.close()
    
    