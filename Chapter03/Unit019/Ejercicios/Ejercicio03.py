"""
Enunciado: Escribe una función map que convierta una lista llamada a_list, la cual contiene letras minúsculas como ['a', 'b', 'c', 'd'], en una lista llamada upper_a_list que contenga las mismas letras en mayúsculas: ['A', 'B', 'C', 'D'].
"""

# Definimos la función de conversión
def to_upper(letra):
    return letra.upper()

a_list = ['a', 'b', 'c', 'd']

# Aplicamos map para transformar cada elemento
upper_a_list = list(map(to_upper, a_list))

print(f"upper_a_list = {upper_a_list}")