###
# RESUMEN COMPLETO: MERGE SORT (BÁSICO Y OPTIMIZADO)
# Basado en la técnica Divide-and-Conquer.
###

# ---------------------------------------------------------
# SECCIÓN 1: IMPLEMENTACIÓN CON MEMORIA ADICIONAL
# ---------------------------------------------------------

def merge1(S, L, R):
    """Mezcla dos listas físicas L y R en S."""
    k = 0
    # Compara y extrae el menor de los frentes (Balanza)
    while len(L) > 0 and len(R) > 0:
        if L[0] <= R[0]:
            S[k] = L.pop(0)
        else:
            S[k] = R.pop(0)
        k += 1

    # Si una lista se agota, añade el resto de la otra
    while len(L) != 0: S[k] = L.pop(0); k += 1
    while len(R) != 0: S[k] = R.pop(0); k += 1

def mergesort1(S):
    """Divide la lista creando sub-listas físicas (slicing)."""
    n = len(S)
    if n > 1:
        mid = n // 2
        L, R = S[:mid], S[mid:] # Se crean nuevas listas en memoria
        mergesort1(L)
        mergesort1(R)
        merge1(S, L, R)

# ---------------------------------------------------------
# SECCIÓN 2: MEJORADO (ENHANCED MERGE SORT)
# Trabaja con rangos de índices en lugar de sublistas.
# ---------------------------------------------------------

def merge2(S, low, mid, high):
    """Mezcla elementos de S usando rangos low-mid y mid-high."""
    R = [] # Lista temporal para la mezcla
    i, j = low, mid + 1

    # Mezcla ordenada basándose en los índices i y j
    while i <= mid and j <= high:
        if S[i] < S[j]:
            R.append(S[i]); i += 1
        else:
            R.append(S[j]); j += 1

    # Añade elementos restantes si un lado terminó antes
    if i > mid:
        for k in range(j, high + 1): R.append(S[k])
    else:
        for k in range(i, mid + 1): R.append(S[k])

    # Copia los elementos mezclados de vuelta a la lista original S
    for k in range(len(R)):
        S[low + k] = R[k]

def mergesort2(S, low, high):
    """Versión eficiente: no divide S en L y R, solo usa índices."""
    if low < high:
        mid = (low + high) // 2
        mergesort2(S, low, mid)      # Mitad izquierda
        mergesort2(S, mid + 1, high)  # Mitad derecha
        merge2(S, low, mid, high)    # Mezcla in-place

# --- Pruebas ---
if __name__ == "__main__":
    datos = [27, 10, 12, 20, 25, 13, 15, 22]

    print("--- Versión Mejorada ---")
    mergesort2(datos, 0, len(datos) - 1) # Llamada con rangos
    print(f"Resultado final: {datos}")