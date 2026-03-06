# Mínimo de pesajes: 2 (3^2 = 9, que es >= 8 monedas)
def ejercicio01(monedas):
    # Paso 1: Dividir en grupos de 3, 3 y 2. Pesar los dos grupos de 3.
    # Supongamos que monedas es una lista de pesos
    g1, g2, g3 = monedas[0:3], monedas[3:6], monedas[6:8]

    if sum(g1) > sum(g2):
        candidatas, inicio = g1, 1
    elif sum(g2) > sum(g1):
        candidatas, inicio = g2, 4
    else:
        candidatas, inicio = g3, 7

    # Paso 2: Pesar las candidatas restantes
    if len(candidatas) == 3:
        if candidatas[0] > candidatas[1]: return inicio
        if candidatas[1] > candidatas[0]: return inicio + 1
        return inicio + 2
    else:
        return inicio if candidatas[0] > candidatas[1] else inicio + 1

# Prueba
print(f"Moneda pesada: {ejercicio01([1,1,1,1,1,1,1.5,1])}")