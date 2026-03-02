"""
Encuentra el piso más alto donde un huevo no se rompe utilizando búsqueda binaria.
El programa debe recibir la altura del edificio y el piso real de ruptura.
"""

def do_experiment(floor, breaking):
    """Retorna True si el huevo se rompe."""
    return floor >= breaking

def find_highest_safe_floor2(height, breaking):
    """Encuentra el piso más alto seguro usando búsqueda binaria."""
    low, high = 1, height

    while low < high:
        mid = (low + high) // 2
        if do_experiment(mid, breaking):
            high = mid
        else:
            low = mid + 1

    return low - 1 # Retorna el último piso donde no se rompió

# Prueba del ejercicio
h = int(input("Input the number of floors: "))       # Ejemplo: 100
b = int(input("Input the first breaking floor: "))  # Ejemplo: 51

floor = find_highest_safe_floor2(h, b)
print(f"Your egg will safe till the {floor}-th floor.")