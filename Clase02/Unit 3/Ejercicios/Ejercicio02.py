"""
Calcula la circunferencia y el area del circulo usando los operadores que hemos estudiado en la unidad
"""
import math

r = int(input("Introdice el radio de la circunferencia"))
pi = math.pi

circunferencia = 2 * pi * r
area = pi * pow(r,2)

print(f"Radio {r}")
print(f"La circunferencia del circulo es {circunferencia}")
print(f"El area del cuadrado es {area}")