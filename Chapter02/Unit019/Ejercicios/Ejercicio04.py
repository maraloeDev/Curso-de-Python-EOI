"""
Enunciado: Calcula la suma de los números enteros del 1 al 100 usando la función reduce y una expresión lambda dentro de ella. Utiliza range(1, 101) como entrada.

Condición de ejecución: Suma del 1 al 100 : 5050.

Tiempo estimado: 5 Minutos.
"""

from functools import reduce # Necesario para Q4

# --- Solución Q3 (map) ---
def to_upper(letra):
    return letra.upper()

a_list = ['a', 'b', 'c', 'd']
upper_a_list = list(map(to_upper, a_list))
print(f"upper_a_list = {upper_a_list}")

# --- Solución Q4 (reduce) ---
# reduce aplica la función acumulativamente a los ítems del rango
suma_total = reduce(lambda x, y: x + y, range(1, 101))
print(f"Suma de 1 a 100 : {suma_total}")