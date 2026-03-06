# Mínimo de pesajes: 2 (3^2 = 9, exacto para 9 monedas)
def ejercicio02(monedas):
    # Paso 1: Dividir en 3 grupos iguales (3, 3, 3)
    g1, g2, g3 = monedas[0:3], monedas[3:6], monedas[6:9]

    if sum(g1) > sum(g2):
        final, offset = g1, 1
    elif sum(g2) > sum(g1):
        final, offset = g2, 4
    else:
        final, offset = g3, 7

    # Paso 2: Pesar 2 del grupo de 3
    if final[0] > final[1]: return offset
    if final[1] > final[0]: return offset + 1
    return offset + 2

print(f"Moneda pesada: {ejercicio02([1,1,1,1,1,1,1,1,1.2])}")