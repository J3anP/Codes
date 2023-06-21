import threading
import time

# Definimos una función que será ejecutada por el thread
def contar_hasta(numero, hilo):
    for i in range(1, numero+1):
        print(f"Contador: {i} del hilo {hilo}")
        time.sleep(0.5)  # Hacemos una pausa de 0.5 segundos

# Creamos dos threads que ejecutarán la función "contar_hasta"
thread1 = threading.Thread(target=contar_hasta, args=(5,1))
thread2 = threading.Thread(target=contar_hasta, args=(3,2))

# Iniciamos los threads
thread1.start()
thread2.start()

# Esperamos a que los threads finalicen
thread1.join()
thread2.join()

print("Finalizado")
