import socket
import numpy as np
import matplotlib.pyplot as plt
import pickle
import time

def guardar_imagen_como_png(img_array):
	"""
	Descripcion de la funcion: Recibe como parámetro de entrada el arreglo bidimensional de la imagen en negativo
	y lo guarda en el disco duro en formato .png
	:entradas:
	img_array: Arreglo bidimensional de la imagen en negativo
	"""
	plt.imshow(img_array, cmap='gray')
	plt.axis('off')
	plt.savefig('imagen_en_negativo.png', bbox_inches='tight')



if __name__ == "__main__":
	inicio_carga = time.perf_counter()
	imagen = np.load('lena_64x64.npy')
	fin_carga = time.perf_counter()

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = ('127.0.0.1',5000)
		print(f"Conectando a {server_address[0]}:{server_address[1]}")

		sock.connect(server_address)
		print("Conexión exitosa")

		inicio_Repecion = time.perf_counter()
		sock.sendall(pickle.dumps(imagen))
		imagen_negativo = pickle.loads(sock.recv(12288))
		fin_Recepcion = time.perf_counter()
		guardar_imagen_como_png(imagen_negativo)

		print(f"El tiempo que demora en cargar la imagen del disco duro a la RAM es de {fin_carga-inicio_carga} segundos")
		print(f"El tiempo que demora el cliente en enviar, recibir y guardar la imagen es de {fin_Recepcion-inicio_Repecion} segundos")
	except ConnectionRefusedError:
		print('No se pudo conectar al servidor')
	finally:
		sock.close()

