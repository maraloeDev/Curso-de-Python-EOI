"""
Pide al usuario el valor del radio y muestra por consola la circunferencia y el area del circulo
"""
import math
radio = int(input("Introduce el radio: "))
circuferencia = 2 * math.pi * radio
area = math.pi * pow(radio,2)
print(f"Circunferencia del circulo = {round(circuferencia,2)}\nArea del circulo = {round(area,2)} ")