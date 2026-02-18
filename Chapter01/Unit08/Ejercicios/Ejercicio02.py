"""
Usa la suma acumulativa para calcular e imprimir la suma de los números enteros del 1 al 100.
(Pista: asegúrate de que el rango de la función range vaya de 1 a 100).
"""

total = 0

for i in range(1, 101):
    total += i

print(f"Sum of integers from 1 to 100: {total}")