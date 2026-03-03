"""
ENUNCIADO:
Escriba un algoritmo que encuentre el K-ésimo elemento más grande, dados N elementos
desordenados. Después de resolver el problema con los dos métodos siguientes,
analice cuál algoritmo es más eficiente:
1. Puede devolver el K-ésimo elemento después de usar la función de ordenamiento (sort).
2. Puede usar la función partition() para realizar una llamada recursiva hasta que
   el pivote sea el K-ésimo elemento.
"""

def find_kth_largest_v1(nums, k):
    """
    MÉTODO 1: Ordenar la lista completa.
    Complejidad: O(N log N) debido al algoritmo de ordenamiento.
    """
    nums_sorted = sorted(nums, reverse=True) # Orden descendente
    return nums_sorted[k-1]

def partition(S, low, high):
    # Lógica de partición estándar de Quick Sort
    pivot = S[low]
    left = low + 1
    right = high
    while left <= right:
        while left <= right and S[left] <= pivot:
            left += 1
        while left <= right and S[right] >= pivot:
            right -= 1
        if left < right:
            S[left], S[right] = S[right], S[left]
    S[low], S[right] = S[right], S[low]
    return right

def find_kth_largest_v2(nums, low, high, k):
    """
    MÉTODO 2: Quickselect (Uso recursivo de partition).
    Complejidad Promedio: O(N). Es más eficiente porque no ordena toda la lista.
    """
    # El K-ésimo más grande en una lista de tamaño N es el índice (N - k)
    target_index = len(nums) - k

    pivot_idx = partition(nums, low, high)

    if pivot_idx == target_index:
        return nums[pivot_idx]
    elif pivot_idx > target_index:
        return find_kth_largest_v2(nums, low, pivot_idx - 1, k)
    else:
        return find_kth_largest_v2(nums, pivot_idx + 1, high, k)

# Ejemplo de prueba
lista = [15, 10, 12, 20, 25, 13, 22]
k = 2 # Queremos el segundo más grande (que sería 22)

print(f"Método 1 (Sort): {find_kth_largest_v1(lista, k)}")
print(f"Método 2 (Partition): {find_kth_largest_v2(lista, 0, len(lista)-1, k)}")

"""
ANÁLISIS DE EFICIENCIA:
El Método 2 es generalmente más eficiente. Mientras que el Método 1 ordena 
absolutamente todos los elementos (O(N log N)), el Método 2 (Quickselect) 
descarta partes de la lista en cada paso, logrando un tiempo de ejecución 
promedio de O(N).
"""