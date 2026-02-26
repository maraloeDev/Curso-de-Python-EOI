"""
Escribe un programa para contar cuántas veces se usó una palabra específica en la oración ingresada por el usuario.
Instrucciones:
En la oración ingresada por el usuario, una palabra se distingue por la presencia de espacios.

Usa la función input().split() para crear la lista S que tenga cada cadena como su elemento.

Usa la función input() para recibir la palabra que será buscada por el usuario y guárdala en x.

La función word_count() recibe S y x como parámetros y devuelve un resultado contando cuántas x están presentes en S.
"""

def word_count(S, x):
    return S.count(x)


S = input("Introduce una frase: ").split()
x = input("Introduce la palabra a buscar: ")

count = word_count(S, x)
print(f"En S, '{x}' apareció {count} veces.")