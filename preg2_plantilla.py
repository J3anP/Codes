import socket,pickle,sys,time
import numpy as np
import matplotlib.pyplot as plt

def guardar_imagen_como_png(img_array):
	plt.imshow(img_array, cmap='gray')
	plt.axis('off')
	plt.savefig('imagen_en_negativo.png', bbox_inches='tight')

if __name__ == "__main__":
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Conectando al servicio de cálculo de imágenes negativas...")
    while True:
        try:
            sock.connect(("localhost",int(sys.argv[1])))
            print("¡Conexión exitosa!")
            break
        except ConnectionRefusedError:
            print("Error de conexión.\nReintentando...")
    while True:
        try:
            ticImagen=time.perf_counter()
            time.sleep(0.1)
            imagen = np.load('lena_64x64.npy')
            tocImagen=time.perf_counter()
            ticEnvioRecepcion=time.perf_counter()
            sock.sendall(pickle.dumps(imagen))
            imagenRecibida=pickle.loads(sock.recv(4248))
        except pickle.UnpicklingError:
             pass
        tocEnvioRecepcion=time.perf_counter()
        guardar_imagen_como_png(imagenRecibida)
        print(f"El tiempo empleado en cargar la imagen del disco a la RAM fue de {tocImagen-ticImagen}s mientras que el tiempo empleado en enviar y recibir la imagen negada fue de {tocEnvioRecepcion-ticEnvioRecepcion}")
        if(input("¿Desea poder trabajar otra imagen? (Escriba 'n' si la respuesta es no):\n> ")=='n'):
            break