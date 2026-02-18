"""
Escribe un programa que reciba la edad como entrada e imprima:

"Adult" (Adulto) si la edad es 20 o más.

"Youth" (Joven) si es menor de 20 y mayor o igual a 10.

"Kid" (Niño) si es menor de 10.
"""

# 1. Solicitamos la edad
age = int(input("Introduce la edad: "))

# 2. Aplicamos la lógica de clasificación
if age >= 20:
    print("Adult")
elif age >= 10:
    # Esta condición solo se revisa si age es menor a 20
    print("Youth")
else:
    # Se ejecuta si es menor a 10
    print("Kid")