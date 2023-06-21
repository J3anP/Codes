import threading
import time

# Creamos una clase que representa un contador
class Contador:
    def __init__(self):
        self.valor = 0
        self.lock = threading.Lock()

    def incrementar(self):
        with self.lock:
            valor_actual = self.valor
            time.sleep(0.1)  # Simulamos un procesamiento lento
            self.valor = valor_actual + 1

# Creamos una instancia del contador
contador = Contador()

# Definimos una función que incrementa el contador en bucle
def incrementar_contador():
    for _ in range(5):
        contador.incrementar()

# Creamos dos threads que ejecutarán la función "incrementar_contador"
thread1 = threading.Thread(target=incrementar_contador)
thread2 = threading.Thread(target=incrementar_contador)

# Iniciamos los threads
thread1.start()
thread2.start()

# Esperamos a que los threads finalicen
thread1.join()
thread2.join()

# Imprimimos el valor final del contador
print("Valor final del contador:", contador.valor)
