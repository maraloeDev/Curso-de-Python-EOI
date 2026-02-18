"""
Escribe el siguiente programa que reciba dos números enteros a y b como entrada,
determine si a es un múltiplo de b e imprima el resultado.
"""

a = int(input("Introduce un numero (a): "))
b = int(input("Introduce un numero (b): "))

es_multiplo = (a % b == 0)
print(f"¿Es {a} múltiplo de {b}?: {es_multiplo}")