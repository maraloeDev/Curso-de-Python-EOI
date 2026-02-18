"""
Cree una lista bidimensional (2D) de tamaño 4 x 4 con valores que vayan del 1 al 16
y envíe a la salida (imprima) todos los elementos utilizando el bucle for.
"""

# Crear la matriz 4x4
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Imprimir usando bucle for
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print() # Salto de línea al terminar cada fila