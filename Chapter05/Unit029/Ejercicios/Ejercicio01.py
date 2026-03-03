"""
ENUNCIADO:
Dada la lista S = [15, 10, 12, 20, 25, 13, 22], escriba el resultado (output)
de la lista S después de ejecutar la función partition1(S, 0, len(S) - 1).
"""

def partition1(S, low, high):
    # Seleccionamos el primer elemento como pivote (15)
    pivot = S[low]
    left = low + 1
    right = high

    # El proceso busca elementos mayores a la izquierda y menores a la derecha
    while left <= right:
        while left <= right and S[left] <= pivot:
            left += 1
        while left <= right and S[right] >= pivot:
            right -= 1

        # Si se encuentran fuera de lugar, se intercambian
        if left < right:
            S[left], S[right] = S[right], S[left]

    # Finalmente, el pivote se coloca en su posición real (índice right)
    S[low], S[right] = S[right], S[low]
    return right

# Ejecución del ejercicio
S = [15, 10, 12, 20, 25, 13, 22]
partition1(S, 0, len(S) - 1)

print("Resultado de la lista tras partition1():")
print(S)
# El resultado será: [13, 10, 12, 15, 25, 20, 22]