import random
import socket

my_IP = "127.0.0.1"
port = 5000

#Diccionario de donde se escoge palabras al azar para el juego
dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]

def letra_mostrar(palabra_random,letra):
    random_word = palabra_random
    hidden_word = '*' * len(palabra_random)
    client_guess = letra
    
    for idx in range(0, len(random_word)):
        if random_word[idx] == client_guess:
            hidden_word = hidden_word[:idx] + client_guess + hidden_word[idx+1:]
    #print("Hidden word: ", hidden_word)
    return hidden_word

if __name__== "__main__":
	# Escriba su codigo aqui    # Esta sentencia no hace nada, solo se ha agregado para que no salga error de sintaxis en la plantilla. Cuando agregue su codigo, puede borrarla.

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((my_IP, port))
    server_socket.listen()
    #cantidad de intentos

    while True:
        client_socket, client_address = server_socket.accept()
        try:
            #data_start = client_socket.recv(1024).decode()
            intentos = 0
            #print("Recibí comando,",data_start)
            palabra_random = random.choice(dictionary)
            print("Palabra elegida: ",palabra_random)

            while intentos<5:
                
                letra = client_socket.recv(1024).decode()
                print("Client guess: ",letra)
                letras_adivinadas = letra_mostrar(palabra_random,letra)
                client_socket.sendall(letras_adivinadas.encode())

                if letra not in palabra_random:
                    intentos += 1

                # Verificar si se adivinó la palabra completa
                if letras_adivinadas == palabra_random:
                    client_socket.sendall('¡Has adivinado la palabra!'.encode())
                    break

            if letras_adivinadas != palabra_random:
                client_socket.sendall(f'Has agotado tus intentos. La palabra era {palabra_random}'.encode())

        finally:
            client_socket.close()

        server_socket.close()