"""
En el ejemplo de salida de abajo, hay una lista que contiene tuplas con elementos,
así como también tuplas vacías, cadenas (strings) vacías y listas vacías que no tienen elementos.
Escribe un código para eliminar estas tuplas vacías, cadenas vacías y listas vacías de la lista proporcionada. (Sin embargo, no elimines la tupla ((),) porque se considera que contiene una tupla vacía).
"""

given_list = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']

filtered_list = []

for item in given_list:

    if item:

        filtered_list.append(item)

print(f"Given list: {given_list}")
print(f"The most frequent element: {filtered_list}") # El ejercicio pide el resultado filtrado