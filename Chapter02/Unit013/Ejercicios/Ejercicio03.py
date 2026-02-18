"""
Escribe un programa que genere un arreglo multidimensional (matriz) de tamaño $n \times n$,
basado en el número ingresado por el usuario (recibiendo un valor de $n$ igual o mayor a dos).
En este caso, el contenido del arreglo debe mostrarse de tal manera que los valores 0 y 1 se intercepten
siguiendo un patrón de tablero de ajedrez.
"""


n = int(input("Enter n: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()