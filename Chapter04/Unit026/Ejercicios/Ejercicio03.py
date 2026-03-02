"""
Añade una función print() dentro de la búsqueda binaria para verificar la complejidad temporal.
Si el huevo se rompe en el piso 51 de un edificio de 100, la búsqueda debe operar 7 veces.
"""

def find_highest_safe_floor_debug(height, breaking):
    low, high = 1, height
    steps = 0

    while low < high:
        steps += 1
        mid = (low + high) // 2
        # Imprime el estado actual para ver la eficiencia
        print(f"Paso {steps}: low={low}, high={high}, mid={mid}")

        if mid >= breaking:
            high = mid
        else:
            low = mid + 1

    return low - 1, steps

# Prueba según la diapositiva
h, b = 100, 51
resultado, total_pasos = find_highest_safe_floor_debug(h, b)

print(f"\nResultado: Piso {resultado}")
print(f"Total de comparaciones: {total_pasos}") # Debería ser 7