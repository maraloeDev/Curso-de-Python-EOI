"""
DEFINICIÓN:
El Ordenamiento por Inserción (Insertion Sort) construye la lista ordenada
final un elemento a la vez. Es muy similar a como ordenamos cartas en la mano.

EXPLICACIÓN (Unidad 27 - Proceso 3.2):
1. Comienza desde el segundo elemento (índice 1).
2. Compara el elemento actual (key) con los de su izquierda.
3. Si el elemento de la izquierda es mayor, lo desplaza una posición a la derecha.
4. El proceso de 'shifteado' continúa hasta encontrar el lugar correcto donde
   'insertar' el valor actual.
"""

def insertion_sort(lista):
    # Empezamos en el segundo elemento, el primero se considera ya 'ordenado'
    for i in range(1, len(lista)):
        key = lista[i] # El valor que queremos insertar
        j = i - 1

        # Mientras el vecino izquierdo sea mayor que nuestra 'key'
        while j >= 0 and lista[j] > key:
            # Desplazamos a la derecha para abrir espacio
            lista[j + 1] = lista[j]
            j -= 1

        # Insertamos el valor en su hueco correcto
        lista[j + 1] = key
    return lista

# Datos del ejemplo
marbles = [50, 30, 40, 10, 20]
print("Insertion Sort Result:", insertion_sort(marbles))