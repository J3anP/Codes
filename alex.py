from threading import Thread
import asyncio
from multiprocessing import Pool
import time

def sumatoria(N):
    suma = 0
    for _ in range(N):
        suma += 1
    return suma
#def sumatoria_asincrona():
   
def sumatoria_thread(ran1,ran2):
    suma= 0
    for _ in range(ran1,ran2):
        suma += 1
    return suma
    
def sumatoria_multiproceso(parte, N):
    suma = 0
    if parte == 0:
        for _ in range(round(N/4)):
            suma+=1
    if(parte == 1):
        for _ in range(round(N/4), round(N/2)):
            suma += 1
    if(parte == 2):
        for _ in range(round(N/2), 3*round(N/4)):
            suma += 1
    if(parte == 3):
        for _ in range(3*round(N/4), N):
            suma += 1
    return suma
            
    
    
if __name__ == '__main__':
    N = 100_000_000
    #Parte serial
    t1 = time.perf_counter()
    suma_s = sumatoria(N)
    t2 = time.perf_counter()
    print(f"El tiempo de ejecución serial es: {t2-t1:.6f} segundos")
    
    #Parte asincrona
    
    
    #Parte multihilo
    t1_m = time.perf_counter()
    sum1 = Thread(target = sumatoria_thread, args = (0,round(N/4)))
    sum2 = Thread(target = sumatoria_thread, args = (round(N/4),round(N/2)))
    sum3 = Thread(target = sumatoria_thread, args = (round(N/2),3*round(N/4)))
    sum4 = Thread(target = sumatoria_thread, args = (3*round(N/4),N))
    
    sum1.start()
    sum2.start()
    sum3.start()
    sum4.start()
    
    sum1.join()
    sum2.join()
    sum3.join()
    sum4.join()
    t2_m = time.perf_counter()
   
    print(f"El tiempo de ejecución con threads es: {t2_m - t1_m:.6f} segundos")
    
    
    #Parte multiproceso/paralelismo
    t1_p = time.perf_counter()
    p = Pool(processes = 4)
    args_p = [(i,N) for i in range(4)]
    partes = p.starmap(sumatoria_multiproceso, args_p)
    p.close()
    p.join()
    suma_p = sum(partes)
    t2_p = time.perf_counter()
    #print(suma_p)
    print(f"Tiempo de ejecución en paralelo es: {t2_p -t1_p:.6f} segundos")