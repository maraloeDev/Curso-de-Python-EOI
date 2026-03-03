def bubblesort(S):
    n = len(S)
    swaps = 0
    for i in range(n):
        print(S)  # Imprime el estado de la lista en cada iteración
        for j in range(n - 1):
            if S[j] > S[j + 1]:
                # Ejecuta el intercambio
                S[j], S[j + 1] = S[j + 1], S[j]
                swaps += 1
    return swaps

# Datos del ejercicio
S = [50, 30, 40, 10, 20]
total_swaps = bubblesort(S)
print(S)
print(f"Total de swaps ejecutados: {total_swaps}")