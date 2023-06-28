import time
from werkzeug.security import check_password_hash
from multiprocessing import Pool, Manager

"""
Esta es la contraseña que usted tiene que adivinar. Está encriptada para que no pueda saber cuál es la respuesta correcta a priori.
Lo que tiene que hacer es generar combinaciones de 3 letras y llamar a la función comparar_con_password_correcto(línea 24 de la plantilla)
"""
contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'


# Arreglo con las letras del abecedario. Puede serle de ayuda, no es obligatorio que lo use
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

"""
Función que sirve para comparar su palabra(cadena de 3 caracteres) con la contraseña correcta.
Entrada: Su cadena de 3 caracteres
Salida: True(verdadero) si es que coincide con la contraseña correcta, caso contrario retorna False(falso)
"""


#vocales_list = ["a","e","i","o","u"]

def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

def adivinar_contrasena(vector_vocales):
    for vocal1 in vector_vocales:
        for vocal2 in vector_vocales:
            for letra in abecedario:
                posible_contrasena = vocal1+vocal2+letra
                if comparar_con_password_correcto(posible_contrasena):
                    return posible_contrasena
                              
def adivinar_contrasena_paralela(vocal1,vector_vocales, encontrado):
    for vocal2 in vector_vocales:
        for letra in abecedario:
            posible_contrasena = vocal1+vocal2+letra
            if not encontrado.value:
                if comparar_con_password_correcto(posible_contrasena):
                    return posible_contrasena
            
if __name__ == "__main__":
    vector_vocales = ["a","e","i","o","u"]
    #parte a
    t1_s = time.perf_counter()
    contrasena_serial = adivinar_contrasena(vector_vocales)
    t2_s = time.perf_counter()
    #print(contrasena_serial)
    print(f"El tiempo de ejecución serial para adivinar la contraseña es: {t2_s - t1_s:.4f} segundos")
    
    #parte b
    manager = Manager()
    encontrado = manager.Value('b', False)
    t1_p = time.perf_counter()
    p = Pool(processes=5)
    args = [(vector_vocales[i], vector_vocales, encontrado) for i in range(5)]
    contrasena_paralela = p.starmap(adivinar_contrasena_paralela, args)
    p.close()
    p.join()
    t2_p = time.perf_counter()
    #res = list(filter(None, contrasena_paralela))
    #print(res[0])
    #print(contrasena_paralela)
    print(f"El tiempo de ejecución paralela para adivinar la contraseña es: {t2_p-t1_p:.4f} segundos")
    
    print(f"El speed up del proceso es: {(t2_s-t1_s)/(t2_p - t1_p):.6f}")
