"""
DEFINICIÓN:
El Ordenamiento Burbuja (Bubble Sort) es un algoritmo sencillo que funciona
revisando cada elemento de la lista con el siguiente, intercambiándolos
si están en el orden incorrecto (el mayor a la izquierda).

EXPLICACIÓN (Unidad 27 - Proceso 1.2):
1. Se comparan elementos adyacentes (vecinos).
2. Si el elemento de la izquierda es mayor que el de la derecha, se hace un 'swap'.
3. Al final de la primera pasada, el número más grande 'flota' como una burbuja
   hasta la última posición.
4. En cada nueva pasada, se ignora el último elemento ya ordenado.
"""

def bubble_sort(lista):
    n = len(lista)
    # Bucle externo para recorrer toda la lista
    for i in range(n):
        # El bucle interno llega hasta n-i-1 porque los últimos i ya están ordenados
        for j in range(0, n - i - 1):
            # Comparación de elementos adyacentes
            if lista[j] > lista[j + 1]:
                # Intercambio (Swap)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Datos del ejemplo: Canicas de hierro [50, 30, 40, 10, 20]
marbles = [50, 30, 40, 10, 20]
print("Bubble Sort Result:", bubble_sort(marbles))