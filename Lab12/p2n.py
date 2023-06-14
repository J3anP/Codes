import asyncio
import random as rd
PRECIO_MINIMO = 20_000
T_MAX = 60
import numpy as np
async def reoferta(pujante):
    while True:
        await asyncio.sleep(rd.randint(0,10))
        index = ord(pujante)-97
        mayor = max(reofertas)
        if(reofertas[index]<= mayor):
            nuevo_min = mayor+500
            reofertas[index] = rd.randint(nuevo_min,int(nuevo_min*1.2))
            pujantes[index] = pujante
            print(f"Participante {pujante} hizo reoferta de {int(reofertas[index])}")        

    
async def main():
    async with asyncio.timeout(T_MAX):
        await asyncio.gather(reoferta("a"),
                             reoferta("b"),
                             reoferta("c"),
                             reoferta("d"),
                             reoferta("e"))


if __name__ == "__main__":
    reofertas = np.ones(5)*PRECIO_MINIMO
    pujantes = [1,1,1,1,1]
    lista = []
    try:
        asyncio.run(main())
    except TimeoutError:
        print(f"Ofertas finales: ", end="")
        for i in range(5):
            print(f" {pujantes[i]}: {int(reofertas[i])}, ", end = "")
            lista.append([pujantes[i], reofertas[i]])
        print("\n")
        idx,maxv = max(lista, key = lambda item: item[1])
        print(f"El ganador es: {idx}")
            


