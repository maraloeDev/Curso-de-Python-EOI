def insertionsort2(S):
    n = len(S)
    comparisons = 0
    for i in range(1, n):
        print(S)  # Estado inicial de cada paso [cite: 15]
        x = S[i]
        j = i - 1

        # Simulación de la comparación del bucle while [cite: 15]
        while j >= 0:
            comparisons += 1
            if S[j] > x:
                S[j + 1] = S[j]
                j -= 1
            else:
                break
        S[j + 1] = x
    return comparisons

# Datos del ejercicio [cite: 15]
S = [50, 30, 40, 10, 20]
total_comps = insertionsort2(S)
print(S)
print(f"Total de comparaciones ejecutadas: {total_comps}")