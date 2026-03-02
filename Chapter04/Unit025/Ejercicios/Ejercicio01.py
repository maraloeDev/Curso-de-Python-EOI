def search_insert_position(nums, x):
    """
    Implementación de búsqueda binaria para encontrar el índice
    donde se debe insertar 'x' manteniendo el orden de la lista.
    """
    low = 0
    high = len(nums)  # Se usa len(nums) porque el índice de inserción puede ser al final

    while low < high:
        mid = (low + high) // 2  # Cálculo del punto medio

        if nums[mid] < x:
            low = mid + 1  # Si el valor es menor, buscamos en la mitad derecha
        else:
            high = mid     # Si es mayor o igual, buscamos en la mitad izquierda

    return low

# --- Código del enunciado Q1 ---
nums = [10, 20, 40, 50, 60, 80]
x = int(input("Input a number to insert: "))

# 1. Encontrar la posición correcta
pos = search_insert_position(nums, x)
print(f"{x} should be inserted at position {pos}.")

# 2. Insertar el número para verificar el resultado
nums.insert(pos, x)
print(nums)