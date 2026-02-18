"""
La siguiente tupla registra las ventas diarias de una tienda durante 10 días.
Escriba un código para imprimir cuántos días tuvieron ventas reducidas en comparación con el día anterior.
 Pista: compare los valores iterando los elementos con una sentencia de iteración).
"""

ventas = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
dias_reducidos = 0

for i in range(1, len(ventas)):
    if ventas[i] < ventas[i-1]:
        dias_reducidos += 1

print("Días con ventas reducidas:", dias_reducidos)