"""
Se dan una letra '1' y tres '0'.
Utiliza estas dos para formar el número 1000.
Aquí, solo se pueden usar operaciones de suma entre cadenas (strings), y la función int() se puede usar solo una vez.
"""

letra1 = "1"
letra2 = "0"
print(int(letra1 + letra2 * 3))