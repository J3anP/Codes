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
	timezone_dict = {'uk': ['UK', 0 * 3600], 'es': ['España', 1 * 3600],
	                 'hk': ['Hong Kong', 8 * 3600], 'jp': ['Japón', 9 * 3600],
	                 'us': ['Estados Unidos', -5*3600]}
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
    
    
def bolsa_proxima(servidores_ntp):
    pais_dif_hora = {"UK": None, "España": None, "EE.UU": None, "Hong Kong": None, "Japón": None}
    
    fechas = list()
    for host in servidores_ntp:
        fechas.append(get_ntp_time(host))
        
    peru_date_hoy = datetime.datetime.today()
    for pais,date in zip(pais_dif_hora.keys(), fechas):
        hoy = peru_date_hoy.day
        if date.hour >= 8:
            hoy += 1 #si un pais ya pasó las 8am, pero los demás no
        apertura_date = datetime.datetime(peru_date_hoy.year,peru_date_hoy.month,peru_date_hoy.day,8,0,0)
        pais_dif_hora[pais] = apertura_date - date

    for pais in pais_dif_hora.keys():
        if pais_dif_hora[pais] == min(pais_dif_hora.values()):
            print(f"El pais proximo a abrir es: {pais}")
            
def bolsa_proxima_threads(pais,host):
    global pais_dif_hora_dic
    date_peru = datetime.datetime.today()
    hoy_peru = date_peru.day
    date_pais = get_ntp_time(host)
    if date_pais.hour>=8:
        hoy_peru+=1
    apertura_date = datetime.datetime(date_peru.year,date_peru.month,hoy_peru,8,0,0)
    pais_dif_hora_dic[pais] = apertura_date - date_pais
    time.sleep(0.001)
    
if __name__ == '__main__':
    #Parte a
    inicio = time.perf_counter()
    bolsa_proxima(servidores_ntp)
    fin = time.perf_counter()
    
    print(f"El tiempo de ejecución sin threads es: {fin-inicio} segundos")
    
    #Parte b
    pais_dif_hora_dic = {"UK": 0, "España": 0, "EE.UU": 0, "Hong Kong": 0, "Japón": 0}
    fecha_UK = Thread(target = bolsa_proxima_threads, args = ("UK",servidores_ntp[0]))
    fecha_spain= Thread(target = bolsa_proxima_threads, args = ("España",servidores_ntp[1]))
    fecha_EEUU= Thread(target = bolsa_proxima_threads, args = ("Estados Unidos",servidores_ntp[2]))
    fecha_HK = Thread(target = bolsa_proxima_threads, args = ("Hong Kong",servidores_ntp[3]))
    fecha_japon= Thread(target = bolsa_proxima_threads, args = ("Japón",servidores_ntp[4]))
    
    ini_t= time.perf_counter()
    fecha_UK.start()
    fecha_spain.start()
    fecha_EEUU.start()
    fecha_HK.start()
    fecha_japon.start()
    
    fecha_UK.join()
    fecha_spain.join()
    fecha_EEUU.join()
    fecha_HK.join()
    fecha_japon.join()
    
    mas_proximo = min(pais_dif_hora_dic.values())
    for pais in pais_dif_hora_dic.keys():
        if pais_dif_hora_dic[pais] == mas_proximo:
            print(f"El pais proximo a abrir es: {pais}")
            
    fin_t = time.perf_counter()
    
    print(f"El tiempo de ejecución con threads es: {fin_t - ini_t}")
    
      