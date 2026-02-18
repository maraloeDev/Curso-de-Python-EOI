"""
Recibe un número entero de 3 dígitos del usuario.
Si el dígito de las centenas del número $n$ es $3$, devuelve True (Verdadero). Si no, devuelve False (Falso).
"""

number = int(input("Introduce un numero entero de 3 digitos: "))
es_centena = number // 100

# 3. Comprobar si es igual a 3 y mostrar el resultado
print(es_centena == 3)