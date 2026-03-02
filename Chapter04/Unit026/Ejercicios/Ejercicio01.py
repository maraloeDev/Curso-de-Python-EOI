"""
Dada una lista ordenada nums y un entero x, implementa la función que devuelva el índice donde x debería ser insertado
para que la lista siga estando ordenada después de la inserción.
"""

def search_insert_position(nums, x):
    low = 0
    high = len(nums)

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

# Prueba del ejercicio
nums = [10, 20, 40, 50, 60, 80]
x = int(input("Input a number to insert: ")) # Ejemplo: 30

pos = search_insert_position(nums, x)
print(f"{x} should be inserted at position {pos}.")

nums.insert(pos, x)
print(f"Lista actualizada: {nums}")