"""
Un número palíndromo se refiere a un número entero cuyo valor es el mismo que su valor original,
incluso si se escribe al revés, como 121 o 3443.
Escribe el siguiente programa para determinar si el número es un palíndromo o no, recibiendo el número "n" del usuario.
"""

n = input("Introduce un número: ")

if n == n[::-1]:
    print(f"{n} es un numero palindromo")
else:
    print(f"{n} no es un numero palindromo")