def bubblesort(S):
    n = len(S)
    swap_count = 0  # Inicializamos el contador

    for i in range(n):
        print(f"Iteración {i}: {S}")
        for j in range(n - 1):
            if S[j] > S[j + 1]:
                S[j], S[j + 1] = S[j + 1], S[j]
                swap_count += 1

    return swap_count

S = [50, 30, 40, 10, 20]

total_swaps = bubblesort(S)

print("-" * 20)
print(f"Resultado final: {S}")
print(f"Número total de intercambios: {total_swaps}")