import time
from multiprocessing import Pool, cpu_count

def polinomio(x): #parte a
    f = 0
    for i in range(10_000):
        f += (i+1)*(x**(i+1))
    return f
def polinomio_paralelo(x,i,f): #parteb
    f[i] = (i+1)*(x**(i+1))
    return f[i]
    
if __name__ == '__main__':
    #parte a
    t1_s = time.perf_counter()
    resultado_serial = polinomio(2023)
    t2_s = time.perf_counter()
    print(f"El tiempo de ejecución serial que demora en calcular f(2023) es {t2_s - t1_s:.4f} segundos")
    #parte b
    t1_p = time.perf_counter()
    vect_f = [0] * 10_000
    p = Pool(processes=4)
    args = [(2023,i,vect_f) for i in range(10_000)]
    partes_poli = p.starmap(polinomio_paralelo, args)
    #zip(repeat(2023),vect_i,vect_f)
    p.close()
    p.join()
    resultado_paralelo = sum(partes_poli)
    t2_p = time.perf_counter()
    print(f"El tiempo de ejecución en paralelo que demora en calcular f(2023) es {t2_p - t1_p:.4f} segundos")
    #tiempo sin mejor/tiempo con mejora
    print(f"El valor del speed up es: {(t2_s - t1_s)/(t2_p-t1_p):.6f}")
    
    assert resultado_serial == resultado_paralelo
    
    
