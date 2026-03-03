def partition1(S, low, high):
    pivot = S[low]
    left = low + 1
    right = high

    while True:
        # Mover puntero izquierdo [cite: 23]
        while left <= right and S[left] <= pivot:
            left += 1
        # Mover puntero derecho [cite: 23]
        while left <= right and S[right] >= pivot:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
        else:
            break

    # Colocar el pivote en su posición final [cite: 23]
    S[low], S[right] = S[right], S[low]
    return right

# Datos del ejercicio [cite: 23]
S = [15, 10, 12, 20, 25, 13, 22]
partition1(S, 0, len(S) - 1)
print(f"Resultado después de partition1: {S}")