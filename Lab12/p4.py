import asyncio
import random as rd
import numpy as np
MIN = 15
async def ronda(idx):
    while True:
        await asyncio.sleep(rd.randint(0,10))
        mayorblock= preciosMayoresRonda(ofertas)
        reofertas = [0,0,0]
        participante = "Telefonía"*(idx==0) +"Claro"*(idx==1) + "Entel"*(idx==2)
        copymax = 0
        for n in range(3):
            if(ofertas[idx][n] <= mayorblock[n]):
                reofertas[n] = 1
                if mayorblock[n] >=copymax:
                    copymax = mayorblock[n]
                    
        if reofertas[0]:
            if reofertas[1]:
                if reofertas[2]:
                    ofertas[idx][0:3] = int((copymax +0.5)*(np.random.rand()*0.2 +1))
                    print(f"Participante {participante} hizo reoferta de {ofertas[idx][0]} para los bloques 0, 1 y 2")
                else:
                    ofertas[idx][0:2] = int((copymax +0.5)*(np.random.rand()*0.2+1))
                    print(f"Participante {participante} hizo reoferta de {ofertas[idx][0]} para los bloques 0 y 1")
            else:
                if reofertas[2]:
                    puja =int((copymax +0.5)*(np.random.randint()*0.2+1))
                    ofertas[idx][0] = puja
                    ofertas[idx][2] = puja
                    print(f"Participante {participante} hizo oferta de {puja} para bloques 0 y 2")
                else:
                    ofertas[idx][0] = int((copymax +0.5)*(np.random.randint()*0.2+1))
                    print(f"Participante {participante} hizo oferta de {ofertas[idx][0]} para el bloque 0")
        else:
            if reofertas[1]:
                if reofertas[2]:
                    ofertas[idx][1:3] = int((copymax + 0.5)*(np.random.randint()*0.2+1))
                    print(f"Participante {participante} hizo oferta de {ofertas[idx][1]} para los bloques 1 y 2")
                else:
                    ofertas[idx][1] = int((copymax +0.5)*(np.random.randint()*0.2+1))
                    print(f"Participante {participante} hizo oferta de {ofertas[idx][1]} para el bloque 1")
            else:
                if reofertas[2]:
                    ofertas[idx][2] = int((copymax + 0.5)*(np.random.randint()*0.2+1))
                    print(f"Participante {participante} hizo oferta de {ofertas[idx][2]} para el bloque 2")

async def main():
    async with asyncio.timeout(30):
        await asyncio.gather(ronda(0),ronda(1),ronda(2))
    
def preciosMayoresRonda(ofertas):
    block0 = np.max([ofertas[0][0],ofertas[1][0],ofertas[2][0]])
    block1 = np.max([ofertas[0][1],ofertas[1][1],ofertas[2][1]])
    block2= np.max([ofertas[0][2],ofertas[1][2],ofertas[2][2]])
    return [block0,block1,block2]
    
def ganadoresSubasta(ofertas):
    mayores = preciosMayoresRonda(ofertas)
    if(ofertas[0][0] == mayores[0] or ofertas[0][1] == mayores[1] or ofertas[0][2] == mayores[2] ):
        return "Telefonica"
    if(ofertas[1][0] == mayores[0] or ofertas[1][1] == mayores[1] or ofertas[1][2] == mayores[2] ):
        return "Claro"
    if(ofertas[2][0] == mayores[0] or ofertas[2][1] == mayores[1] or ofertas[2][2] == mayores[2]):
        return "Entel"
    

        
if __name__ == '__main__':
    Telefonia = np.ones((3))*MIN
    Claro = np.ones((3))*MIN
    Entel = np.ones((3))*MIN
    
    ofertas = [Telefonia, Claro, Entel]
    for i in range(3):
        try:
            ganadoresRonda = preciosMayoresRonda(ofertas)
            print(f"Ronda {i+1}: ")
            print("Precios actuales:")
            print(f"Bloque 0: {ganadoresRonda[0]}")
            print(f"Bloque 1: {ganadoresRonda[1]}")
            print(f"Bloque 2: {ganadoresRonda[2]}")
            asyncio.run(main())
        except TimeoutError:
            print(f"Se cumplió el tiempo de 30 segundos. Ronda {i+1} finalizada.")
            
print("Los ganadores son: ")    
ganadores = ganadoresSubasta(ofertas)
pujas_ganadoras = preciosMayoresRonda(ofertas)
for i in range(3):
    print(f"Bloque {i}: {ganadores[i]} con ${pujas_ganadoras[i]}")