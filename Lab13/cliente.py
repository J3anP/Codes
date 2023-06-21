import socket
import sys
from threading import Thread
import time 

def lectura_data(sock):
    while True:
        data = sock.recv(1024).decode('utf-8')
        if data:
            #print(data)
            procesador_thread = Thread(target=procesador, args = (data,))
            procesador_thread.start()
            procesador_thread.join()
            time.sleep(1)
        else:
            break
           
def procesador(data):
    elementos_separados = data.split(';')
    #variables = [elementos_separados[3],elementos_separados[4],elementos_separados[5]]
    variables = elementos_separados[3:]
    #datos = list()
    #for valor in variables:
        #datos.append(float(valor))
    datos = [float(x) for x in variables]
    name = elementos_separados[1]; cant = datos[0]; peso = datos[1]; costoU = datos[2]
    costo_total = calcular_costo_total(cant,costoU)
    clasificacion = clasificacion_componente(costo_total)
    
    print(f"----------------Nombre: {name}----------------")
    print(f"Costo total: {costo_total}")
    print(f"Clasificacion por costo: {clasificacion}")
    if costo_total > 75:
        print(f"Número de componentes con costo elevado: {cant}")
        if peso > 100:
            print(f"Número de componentes con costo elevado y con peso mayor a 100g: {cant}")
        else:
            print(f"Número de componentes con costo elevado y con peso mayor a 100g: 0")
    else:
        print(f"Número de componentes con costo elevado: 0")
        print(f"Número de componentes con costo elevado y con peso mayor a 100g: 0")
    
    if costo_total <25:
        print(f"Número de componentes con costo bajo: {cant}")
    else:
       print(f"Número de componentes con costo bajo: 0") 

def calcular_costo_total(cant, precioU):
    return cant*precioU

def clasificacion_componente(costo_total):
    if costo_total <25:
        return "Costo Bajo"
    if costo_total >=25 and costo_total <50:
        return "Costo regular"
    if costo_total>=50 and costo_total<75:
        return "Costo alto"
    if costo_total>=75:
        return "Costo elevado"
      
def main():
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
       sock.connect(("127.0.0.1",5001))
       lectura_thread = Thread(target = lectura_data,args=(sock,))
       lectura_thread.start()
       lectura_thread.join()
       sock.close()        
   except KeyboardInterrupt:
       sys.exit()
       
if __name__ == '__main__':
    main()