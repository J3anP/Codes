import time
from multiprocessing import Process, Manager, Pool
import math

def validar_primo(n):
    lst = list(range(2,int(math.sqrt(n))+1))
    primo = False
    for num in lst:
        if n%num == 0:
            return False
        else:
            primo = True
    return primo

def validar_primo_paralelo(n,part):
    lst1 = list(range(2,int(math.sqrt(n)/2)+1))
    lst2 = list(range(int(math.sqrt(n)/2)+2, int(math.sqrt(n))+1))
    primo1 = None
    primo2 = None
    if part == 1:
        for num in lst1:
            if n%num == 0:
                primo1= False
                break
            else:
                primo1 = True
        return primo1
    elif part==2:
        for num in lst2:
            if n%num == 0:
                primo2 = False
                break
            else:
                primo2 = True
        return primo2
    return primo1 and primo2

def primo_mayor(x,part,encontre_primo):
    
    if x%2 == 0:
        num1 = x+1; num2 = x+3
    if x%2 != 0:
        num1 = x+2; num2 = x+4
      
    if not encontre_primo.value:
        if part == 1:
            posible_primo = num1
            while not encontre_primo.value:
                if validar_primo(posible_primo):
                    print(f"El siguiente número primo encontrado es {posible_primo}")
                    encontre_primo.value = True
                else:
                    posible_primo += 4
                        
        elif part == 2:
            posible_primo = num2
            while not encontre_primo.value:
                if validar_primo(posible_primo):
                    print(f"El siguiente número primo encontrado es {posible_primo}")
                    encontre_primo.value = True
                else:
                    posible_primo +=4
           
if __name__ == '__main__':
    n = 2_345_678_911_111_111
    
    manager = Manager()
    en_primo = manager.Value('b', False)
    #parte a
    t1 = time.perf_counter()
    es_primo = validar_primo(n)
    t2 = time.perf_counter()
    print(es_primo)
    print(f"Tiempo de ejecución para validar si {n} es primo es {t2-t1:.6f} segundos")
    
    #parte b
    t1_p = time.perf_counter()
    p = Pool(processes=2)
    args = [(n,i) for i in range(1,3)]
    es_primo_paralelo = p.starmap(validar_primo_paralelo, args)
    p.close()
    p.join()  
    t2_p = time.perf_counter()
    primo_paralelo = None
    if es_primo_paralelo == [True, True]:
        primo_paralelo = True
    else:
        primo_paralelo = False    
    print(f"Tiempo de ejecución paralela: {t2_p - t1_p:.6f} segundos")

    print(f"El speed up de parte b con respecto a parte a es: {(t2-t1)/(t2_p - t1_p):.6f}")
        
    assert es_primo == primo_paralelo
    
    #parte c
    x = 24
    t1c = time.perf_counter()
    pc = Pool(processes=2)
    args2 = [(x,i,en_primo) for i in range(1,3)]
    next_primo = pc.starmap(primo_mayor, args2)
    pc.close()
    pc.join()
    t2c = time.perf_counter()
    print(f"El tiempo de ejecución es {t2c-t1c:.6f} segundos")
    
    