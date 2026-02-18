"""
La Agencia A está planeando emitir boletos para un auditorio donde se llevará a cabo un concierto de ídolos.
Aquí, el número n es la entrada y el número de asiento se organiza de la siguiente manera:

Se colocan n * n asientos cuando se da n como entrada.
La disposición de los números de asiento se llama matriz de serpiente porque el arreglo aumenta de uno en uno siguiendo
La forma del tronco de una serpiente (zig-zag).

Escribe un programa que produzca arreglos con estos números.
"""

n = int(input("Enter n : "))

for i in range(n):
    # Generamos los números de la fila actual
    # Calculamos el inicio y el fin de los números para esta fila
    start = i * n + 1
    end = (i + 1) * n + 1
    row = list(range(start, end))

    # Si la fila es impar (índice 1, 3, etc.), invertimos la lista
    if i % 2 != 0:
        row.reverse()

    # Imprimimos la fila formateada
    for num in row:
        print(f"{num:2d}", end="  ")
    print() # Salto de línea para la siguiente fila