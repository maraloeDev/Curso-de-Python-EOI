"""
Usa el valor de "paso" (step) de la función range para encontrar la suma de los números pares del 1 al 100.
Pista: Establece el valor inicial en cero y el paso en dos.
"""

suma_pares = 0

for i in range(0, 101, 2):
    suma_pares += i

print(f"Sum of even numbers from 1 to 100: {suma_pares}")