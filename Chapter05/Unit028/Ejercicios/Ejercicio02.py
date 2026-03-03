def mergesort_debug(S, nivel=0):
    n = len(S)
    indent = "  " * nivel
    print(f"{indent}Dividiendo: {S}")

    if n <= 1:
        return S

    mid = n // 2
    L = S[:mid]
    R = S[mid:]

    izq = mergesort_debug(L, nivel + 1)
    der = mergesort_debug(R, nivel + 1)
    return sorted(izq + der)

lista_clase = [27, 10, 12, 20, 25, 13, 15, 22]
print("--- ÁRBOL DE DIVISIÓN ---")
mergesort_debug(lista_clase)