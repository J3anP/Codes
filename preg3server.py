import random,socket,numpy as np

my_IP = "127.0.0.1"
port = 5000
dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]

if __name__ == "__main__":
    # 20213852
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((my_IP,port))
    print(f"Arrancando servidor en {my_IP}:{port}...")
    s.listen(1)
    while True:
        try:
            s.settimeout(0.01)
            print("Esperando una nueva conexión de un cliente")
            while True:
                try:
                    c,cAddress=s.accept()
                    s.settimeout(None)
                    break
                except TimeoutError:
                    pass
            print(f"...conexión de: {cAddress}")
            while True:
                if c.recv(1024).decode()=='start':
                    print("recibi comando start")
                    random_word = dictionary[np.random.randint(len(dictionary))]
                    hidden_word = "*"*len(random_word)
                    c.sendall(hidden_word.encode())
                    contadorAciertos=0
                    while contadorAciertos<len(random_word):
                        client_guess = c.recv(1024).decode()
                        if len(client_guess)==1:
                            for idx in range(len(random_word)):
                                if random_word[idx] == client_guess:
                                    hidden_word = hidden_word[:idx] + client_guess + hidden_word[idx+1:]
                                    contadorAciertos+=1
                                    break
                            c.sendall(hidden_word.encode())
                        elif client_guess=="":
                            print("El usuario se ha desconectado.")
                            break
                    print("¡Partida finalizada!")
                    break
        except KeyboardInterrupt:
            print("El programa se ha interrumpido abrúptamente")
            break