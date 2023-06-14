import time 
import asyncio
import random as rd

PRECIO_MINIMO = 20_000
PRECIO_MAXIMO = 100_000

async def subast(subastante, tiempo):
    await asyncio.sleep(tiempo)
    participantes.append(subastante)
    puja = rd.randint(PRECIO_MINIMO, PRECIO_MAXIMO)
    ofertas.append(puja)
    
async def main():
    await asyncio.gather(subast("a",rd.randint(0,10)),
                         subast("b",rd.randint(0,10)),
                         subast("c",rd.randint(0,10)),
                         subast("d",rd.randint(0,10)),
                         subast("e",rd.randint(0,10)))
    
if __name__ == '__main__':
    ofertas = []
    participantes = []
    lista = []
    
    ini = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()
    
    print(f"Ofertas finales: ", end = " ")
    for i in range(5):
        print(f"{participantes[i]}: {ofertas[i]}, ", end = "")
        lista.append([participantes[i],ofertas[i]])
    print("\n")
    idx, maxv = max(lista, key = lambda item: item[1])
    print(f"El ganador es: {idx}")
    
    print(f"Tiempo que dura la subasta es {fin - ini} segundos")