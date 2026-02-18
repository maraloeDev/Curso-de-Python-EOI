"""
Escribe un código que tome la entrada del usuario y determine si el valor entero
$n$ es un número par dentro del rango de $0$ a $100$ o no.
"""

n = int(input("Introduce un numero: "))

resultado = (n % 2 == 0) and range(0,11)

print(f"El numero {n} esta dentro del rango 0 y 10? = {resultado}")