"""
Escribe un programa que reciba la edad como entrada e imprima:
"Adult" (Adulto) si la edad es $20$ o más.
"Youth" (Joven) si es menor de $20$ y mayor o igual a $10$.
"Kid" (Niño) si es menor de $10$.
"""

age = int(input("Introduce tu edad: "))

if age >= 20:
    print("Adult")
elif 10 <= age < 20:
    print("Youth")
else:
    print("Kid")