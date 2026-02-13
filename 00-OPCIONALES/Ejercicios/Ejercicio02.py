"""
Unit 2: Planning for Programming
"""

#  Básico 1: Escribe en lenguaje natural (pseudocódigo) los pasos para calcular el
# promedio de tres exámenes.

n1 = int(input("Introduce una nota: "))
n2 = int(input("Introduce una nota: "))
n3 = int(input("Introduce una nota: "))
total = n1 + n2 + n3
print(f"El promedio es {total/3}")

# Básico 2: Identifica la entrada, el proceso y la salida para un programa que calcula
# el IVA (21%) de un precio.

nombre_producto = str(input("Introduce el nombre del producto: "))
precio_producto = int(input("Introduce el precio del producto"))
print(f"Total: {precio_producto/21}")

# Medio 1: Dibuja (usando texto) un diagrama de flujo para decidir si llevar paraguas:
# ¿Está lloviendo? SI -> Llevar, NO -> No llevar

