def merge2(S, low, mid, high):
    # Esta función mezcla dos mitades ordenadas
    pass

def mergesort2(S, low, high, counter):
    if low < high:
        mid = (low + high) // 2
        mergesort2(S, low, mid, counter)
        mergesort2(S, mid + 1, high, counter)
        merge2(S, low, mid, high)
        counter[0] += 1  # Incrementa cada vez que se ejecuta la mezcla

# Datos del ejercicio [cite: 19]
S = [6, 2, 11, 7, 5, 4, 8, 16, 10, 3]
ejecuciones = [0]
mergesort2(S, 0, len(S) - 1, ejecuciones)

print(f"La función merge2() se ejecutó {ejecuciones[0]} veces.")