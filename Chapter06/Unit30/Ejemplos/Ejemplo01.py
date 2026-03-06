"""
TEMA: ENFOQUE CODICIOSO (GREEDY APPROACH)
-----------------------------------------
DEFINICIÓN:
Es una técnica de diseño de algoritmos que llega a una solución seleccionando
la "mejor" opción en el momento actual según criterios predefinidos.

PASOS DEL DISEÑO (DISEÑO DEL ALGORITMO):
1. Proceso de Selección: Elegir el mejor elemento para añadir al conjunto.
2. Verificación de Factibilidad: Comprobar si el nuevo conjunto es apropiado
   para ser la respuesta (ej. que no exceda el monto).
3. Verificación de la Solución: Determinar si el conjunto actual resuelve
   el problema por completo.
"""

# =======================================================
# 1. PROBLEMA DEL CAMBIO DE MONEDA (COIN CHANGE PROBLEM)
# =======================================================
# Objetivo: Dar el cambio con el menor número de monedas posible.
# Monedas disponibles (Corea): 500, 100, 50, 10 won.

def coin_change(coins, amount):
    """
    Implementación según diapositiva 1.1.
    Asume que las monedas están en orden descendente.
    """
    changes = [] # Lista que actúa como billetera
    largest = 0  # Posición de la moneda más grande

    while amount > 0:
        if amount < coins[largest]:
            # Verificación de factibilidad fallida: pasa a la siguiente moneda
            largest += 1
        else:
            # Proceso de selección: añade la moneda
            changes.append(coins[largest])
            amount -= coins[largest]

    return changes

# Ejemplo de ejecución (Diapositiva 1.2):
# Para 870 won:
# 1. Selecciona 500 (resta 370)
# 2. Selecciona 100 (resta 270)
# 3. Selecciona 100 (resta 170)
# 4. Selecciona 100 (resta 70)
# 5. Selecciona 50 (resta 20)
# 6. Selecciona 10 (resta 10)
# 7. Selecciona 10 (resta 0) -> Problema resuelto

# =======================================================
# 2. SELECCIÓN DE ACTIVIDADES (ACTIVITY SELECTION)
# =======================================================
# Objetivo: Maximizar el número de reuniones que no se traslapan.
# Regla Greedy: Seleccionar reuniones basándose en el tiempo de fin más rápido.

def activity_selection1(start, finish):
    """
    Implementación según diapositiva 3.2.
    """
    result = []
    i = 0 # Primera reunión (la que termina más rápido)
    result.append(i)

    for j in range(1, len(start)):
        # Si la reunión actual empieza después de que termine la anterior
        if finish[i] <= start[j]:
            result.append(j)
            i = j # Actualiza la última reunión seleccionada

    return result

# Datos del problema (Diapositiva 2.1):
# id:      0  1  2  3  4  5  6
# start:  [1, 3, 2, 1, 5, 8, 5]
# finish: [2, 4, 5, 6, 6, 9, 9]

# =======================================================
# USOS Y CARACTERÍSTICAS
# =======================================================
# - Muy eficiente y simple para problemas de optimización.
# - El resultado final del ejemplo de actividades es [0, 1, 4, 5],
#   logrando un máximo de 4 reuniones.

if __name__ == "__main__":
    # Ejecución Cambio de Moneda
    monedas_corea = [500, 100, 50, 10]
    monto_objetivo = 870
    resultado_monedas = coin_change(monedas_corea, monto_objetivo)

    print(f"Cambio para {monto_objetivo}: {resultado_monedas}")
    print(f"Total de monedas: {len(resultado_monedas)}")

    # Ejecución Selección de Actividades
    s = [1, 3, 2, 1, 5, 8, 5]
    f = [2, 4, 5, 6, 6, 9, 9]
    reuniones = activity_selection1(s, f)

    print(f"\nReuniones seleccionadas (IDs): {reuniones}")
    print(f"Máximo de reuniones posibles: {len(reuniones)}")