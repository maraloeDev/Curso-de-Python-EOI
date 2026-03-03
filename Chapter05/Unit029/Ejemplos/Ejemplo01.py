"""
TEMA: QUICK SORT (ORDENAMIENTO RÁPIDO)
--------------------------------------
DEFINICIÓN:
Es un algoritmo de "Dividir y Vencerás". Funciona seleccionando un elemento
como 'pivote' y partiendo el arreglo alrededor del pivote, de modo que:
1. Los elementos menores que el pivote queden a su izquierda.
2. Los elementos mayores que el pivote queden a su derecha.

EXPLICACIÓN DEL PROCESO (PARTICIÓN):
Como viste en el ejemplo de las canicas y la balanza:
- Se elige un pivote (frecuentemente el primer elemento).
- Se usan dos punteros: 'left' (que busca elementos mayores al pivote)
  y 'right' (que busca elementos menores al pivote).
- Cuando se encuentran, se intercambian (swap).
- Al final, el pivote se coloca en su posición real.
"""

def partition1(S, low, high):
    # Elegimos el primer elemento como pivote (según Diapositiva 1.2)
    pivot = S[low]
    left = low + 1
    right = high

    print(f"\n--- Particionando sub-lista: {S[low:high+1]} ---")
    print(f"Pivote seleccionado: {pivot}")

    while left <= right:
        # 1. Buscar desde la izquierda el primer elemento mayor al pivote
        while left <= right and S[left] <= pivot:
            left += 1

        # 2. Buscar desde la derecha el primer elemento menor al pivote
        while left <= right and S[right] >= pivot:
            right -= 1

        # 3. Si los punteros no se han cruzado, intercambiamos
        if left < right:
            print(f"Swap: {S[left]} (mayor) <-> {S[right]} (menor)")
            S[left], S[right] = S[right], S[left]
            print(f"Estado actual: {S}")

    # 4. Colocar el pivote en su posición final (índice right)
    pivotpoint = right
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    print(f"Pivote {pivot} colocado en posición final: {S}")

    return pivotpoint

def quicksort1(S, low, high):
    """
    Función recursiva principal (Divide y Vencerás)
    """
    if low < high:
        # Obtenemos la posición donde quedó el pivote anterior
        pivotpoint = partition1(S, low, high)

        # Ordenamos recursivamente la parte izquierda
        quicksort1(S, low, pivotpoint - 1)

        # Ordenamos recursivamente la parte derecha
        quicksort1(S, pivotpoint + 1, high)

# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    # Ejemplo de la diapositiva 1.1
    lista_ejemplo = [15, 10, 12, 20, 25, 13, 22]

    print("LISTA ORIGINAL:", lista_ejemplo)

    # Llamamos a quicksort(lista, primer_indice, ultimo_indice)
    quicksort1(lista_ejemplo, 0, len(lista_ejemplo) - 1)

    print("\n-------------------------")
    print("LISTA FINAL ORDENADA:", lista_ejemplo)

"""
CASOS COMUNES Y COMPLEJIDAD:
1. Caso Promedio: O(N log N). Es extremadamente rápido para datos aleatorios.
2. Peor Caso: O(N²). Ocurre si el pivote siempre es el elemento más pequeño o 
   más grande (por ejemplo, si la lista ya está ordenada).
3. Espacio: In-place. A diferencia de Merge Sort, no requiere crear listas 
   nuevas (como viste en la Diapositiva 1.1 de 'In-Place sorting').
"""