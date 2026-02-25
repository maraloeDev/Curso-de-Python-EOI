"""
======================================================================
         DIFERENCIAS: BÚSQUEDA SECUENCIAL VS. BINARIA
======================================================================

1. SECUENCIAL:
   - Recorre todo. No requiere orden.
   - Si tienes 1,000,000 de datos, podría hacer 1,000,000 de comparaciones.

2. BINARIA:
   - Divide en mitades. REQUIERE ORDEN.
   - Si tienes 1,000,000 de datos, la encuentra en máximo 20 pasos.
======================================================================
"""

def busqueda_secuencial(lista, objetivo):
    """Algoritmo que revisa uno por uno."""
    pasos = 0
    for i in range(len(lista)):
        pasos += 1
        if lista[i] == objetivo:
            return i, pasos # Retorna posición y pasos dados
    return -1, pasos

def busqueda_binaria(lista, objetivo):
    """Algoritmo que divide en mitades (Requiere lista ordenada)."""
    pasos = 0
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        pasos += 1
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio, pasos
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1, pasos

# --- PRUEBA DE LOS ALGORITMOS ---

# 1. Creamos una lista ordenada (necesaria para la binaria)
datos = [10, 22, 35, 47, 50, 68, 75, 81, 94, 99]
buscar = 81

print(f"Lista de datos: {datos}")
print(f"Objetivo: {buscar}\n")

# Ejecución Secuencial
pos_s, pasos_s = busqueda_secuencial(datos, buscar)
print(f"[SECUENCIAL] Encontrado en índice: {pos_s} | Pasos realizados: {pasos_s}")

# Ejecución Binaria
pos_b, pasos_b = busqueda_binaria(datos, buscar)
print(f"[BINARIA]    Encontrado en índice: {pos_b} | Pasos realizados: {pasos_b}")

print("\nConclusión: La binaria suele requerir menos pasos en listas ordenadas.")