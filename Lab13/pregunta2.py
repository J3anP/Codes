#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import datetime
from threading import Thread
import socket
import struct
import time

servidores_ntp = [
	"0.uk.pool.ntp.org",    # Londres(Reino Unido)
	"1.es.pool.ntp.org",    # Madrid (España)
	"0.us.pool.ntp.org",    # Nueva York(Estados Unidos)
	"0.hk.pool.ntp.org",    # Hong Kong
	"0.jp.pool.ntp.org"     # Tokyo(Japón)
]

"""
Función: get_ntp_time
Descripción: Imprime la  fecha-hora actual en un país determinado
Entrada: Cualquiera de las URLs definidas en la lista servidores_ntp
Salida: Retorna la fecha-hora(timestamp) en formato datetime.datetime, también la imprime
IMPORTANTE: NO modifique esta funcion 
"""
def get_ntp_time(host):
	timezone_dict = {'uk': ['UK', 1 * 3600], 'es': ['España', 2 * 3600],
	                 'hk': ['Hong Kong', 8 * 3600], 'jp': ['Japón', 9 * 3600],
	                 'us': ['Estados Unidos', -4*3600]}
	key = ''
	port = 123
	buf = 1024
	address = (host, port)
	msg = b'\x1b' + 47 * b'\0'

	# reference time (in seconds since 1900-01-01 00:00:00)
	TIME1970 = 2208988800  # 1970-01-01 00:00:00
	# connect to server
	client = socket.socket(AF_INET, SOCK_DGRAM)
	client.sendto(msg, address)
	msg, address = client.recvfrom(buf)
	t = struct.unpack("!12I", msg)[10]
	t -= TIME1970
	client.close()

	for each_key in timezone_dict:
		if each_key in host:
			key = each_key
			break
	print(f"Hora en {timezone_dict[key][0]}: {datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])}")
	return datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])

def funcion_sincrona(servidores_ntp):
    lista_fechas = []
    diccionario = {'UK': 0, 'España': 0, 'Estados Unidos': 0, 'Hong Kong': 0, 'Japón': 0}
    
    for url in servidores_ntp:
        lista_fechas.append(get_ntp_time(url))
    
    fecha_peru = datetime.datetime.today()
    año = fecha_peru.year
    mes = fecha_peru.month
    
    for pais,fecha in zip(diccionario.keys(),lista_fechas):
        dia = fecha_peru.day
        if fecha.hour >= 8:
            dia += 1
        hora_apertura = datetime.datetime(año,mes,dia,8,0,0)
        diccionario[pais] = hora_apertura - fecha
    
    min_valor = min(diccionario.values())
    for key in diccionario.keys():
        if diccionario[key] == min_valor:
            print(f"El país cuya bolsa está más próxima a abrir con respecto a Perú es: {key}")
            break

def funcion_multihilo(url,pais):
    global diccionario_fechas
    fecha = get_ntp_time(url)
    fecha_peru = datetime.datetime.today()
    año = fecha_peru.year
    mes = fecha_peru.month
    dia = fecha_peru.day
    if fecha.hour >= 8:
        dia += 1
    hora_apertura = datetime.datetime(año,mes,dia,8,0,0)
    diccionario_fechas[pais] = hora_apertura - fecha
    time.sleep(0.01)

if __name__ == '__main__':
    #Implementación síncrona
    print("Implementación síncrona")
    inicio_sincrono = time.perf_counter()
    funcion_sincrona(servidores_ntp)
    fin_sincrono = time.perf_counter()
    print(f"El tiempo de ejecución de la función síncrona es: {fin_sincrono-inicio_sincrono} segundos")
  
    #Implementación con threads
    print("\nImplementación con threads")
    diccionario_fechas = {'UK': 0, 'España': 0, 'Estados Unidos': 0, 'Hong Kong': 0, 'Japón': 0}
    t1 = Thread(target=funcion_multihilo,args=(servidores_ntp[0],"UK"))
    t2 = Thread(target=funcion_multihilo,args=(servidores_ntp[1],"España"))
    t3 = Thread(target=funcion_multihilo,args=(servidores_ntp[2],"Estados Unidos"))
    t4 = Thread(target=funcion_multihilo,args=(servidores_ntp[3],"Hong Kong"))
    t5 = Thread(target=funcion_multihilo,args=(servidores_ntp[4],"Japón"))
    inicio_multihilo = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    min_valor = min(diccionario_fechas.values())
    for key in diccionario_fechas.keys():
        if diccionario_fechas[key] == min_valor:
            print(f"El país cuya bolsa está más próxima a abrir con respecto a Perú es: {key}")
            break
    fin_multihilo = time.perf_counter()
    print(f"El tiempo de ejecución de la función multihilo es: {fin_multihilo-inicio_multihilo} segundos")