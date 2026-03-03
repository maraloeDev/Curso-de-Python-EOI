"""
DEFINICIÓN:
El Ordenamiento por Selección (Selection Sort) mejora ligeramente al anterior
al buscar el elemento más pequeño de la parte desordenada y colocarlo
al principio de la lista.

EXPLICACIÓN (Unidad 27 - Proceso 2.2):
1. El algoritmo divide la lista en dos partes: ordenada (izquierda) y desordenada (derecha).
2. Utiliza una 'balanza' lógica para comparar y encontrar el valor mínimo
   en la sección desordenada.
3. Una vez encontrado el mínimo, lo intercambia con el primer elemento desordenado.
4. Es eficiente en cuanto a intercambios (solo hace uno por cada pasada).
"""

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Suponemos que el actual es el mínimo
        min_idx = i
        # Buscamos en el resto de la lista desordenada
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j

        # Intercambio del mínimo encontrado con la posición actual i
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Datos del ejemplo
marbles = [50, 30, 40, 10, 20]
print("Selection Sort Result:", selection_sort(marbles))