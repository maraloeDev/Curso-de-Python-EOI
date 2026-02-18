"""
Modifiquemos el programa anterior para imprimir todas las etapas del 1 al 9 de la tabla de multiplicar.
Utiliza únicamente la sentencia while.
"""

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i}*{j}={i*j}")
        j += 1
    i += 1