"""
Usa el valor de "paso" (step) de la función range para encontrar la suma de los números impares del 1 al 100.
Pista: Establece el valor inicial en uno y el paso en dos. (Resultado esperado: 2500).
"""

suma_impares = 0

for i in range(1, 101, 2):
    suma_impares += i

print(f"Sum of odd numbers from 1 to 100: {suma_impares}")