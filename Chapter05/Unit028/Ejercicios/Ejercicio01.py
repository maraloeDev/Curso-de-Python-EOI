def merge_balanza(L, R):
    S = [] #Creo una lista vacia para almacenar
    print(f"Mezclando barril L: {L} y barril R: {R}")

# Mientras la longitud de L y la longitud de R es mayor que 0 se comparan
    while len(L) > 0 and len(R) > 0:
        print(f"  Comparando {L[0]} vs {R[0]}...")

        #Si L[0] es menor que R[0]
        if L[0] <= R[0]:
            print(f"  -> {L[0]} es más ligero. Va a la lista nueva.")
            S.append(L.pop(0))
        else:
            print(f"  -> {R[0]} es más ligero. Va a la lista nueva.")
            S.append(R.pop(0))

    if L: S.extend(L)
    if R: S.extend(R)

    return S


barril_azul = [10, 27]
barril_verde = [13, 15]
resultado = merge_balanza(barril_azul, barril_verde)
print(f"\nResultado final ordenado: {resultado}")