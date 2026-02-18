"""
La computadora tiene un número entero aleatorio entre 1 y 100 como el valor de la respuesta correcta.
Cuando el usuario presenta una respuesta,
el programa solo informa si el número entero presentado es mayor o menor en comparación con la respuesta correcta
que tiene almacenada.

Este juego se repite hasta que el usuario responda correctamente.
"""

import random as rndm

# Generamos el número secreto
numero_random = int(rndm.randint(1, 100))
intentos = 0
adivinado = False

print("Adivina un número entre 1 y 100")

# El bucle se repite hasta que 'adivinado' sea True
while not adivinado:
    # Pedimos la respuesta al usuario
    respuesta = int(input("Introduce un número: "))
    intentos += 1

    if respuesta > numero_random:
        print("¡Más bajo! (Lower!)")

    elif respuesta < numero_random:
        print("¡Más alto! (Higher!)")

    else:
        print(f"¡Felicidades! Lo lograste en {intentos} intentos.")
        adivinado = True

