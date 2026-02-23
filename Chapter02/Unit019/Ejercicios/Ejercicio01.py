"""
Hay una lista con valores de elementos enteros llamada n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Devuelve una lista llamada even_list que solo contenga los elementos con valores pares de n_list, utilizando la función filter y la función lambda.

La lista devuelta even_list = [2, 4, 6, 8, 10]

Condiciones para la ejecución: even_list = [2, 4, 6, 8, 10]

Tiempo: 5 Minutos
"""

n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []

for item in filter(lambda x: x % 2 == 0, n_list):
    even_list.append(item)

print(even_list)