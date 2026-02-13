"""
Usa la suma acumulativa para calcular e imprimir la suma de los números enteros del 1 al 100.
 (Pista: haz que el valor de la función range vaya de 1 al 100).

Ejemplo de salida: Suma de enteros del 1 al 100: 5050.
Tiempo estimado: 5 minutos.
"""

suma = 0
for i in range(1, 101) :
    suma+=i

print(f"Suma de enteros del 1 al 100: {suma}")