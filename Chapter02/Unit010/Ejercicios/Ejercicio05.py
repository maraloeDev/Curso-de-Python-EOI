"""
En el ejemplo de salida que se muestra abajo, hay una lista que contiene tuplas con elementos,
así como también tuplas vacías, cadenas (strings) vacías y listas vacías que no tienen elementos.
Escribe un código para eliminar estas tuplas vacías, cadenas vacías y listas vacías de la lista proporcionada.
(Sin embargo, no elimines la tupla ((),) porque se considera que contiene una tupla vacía).
"""
lista_entrada = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']

lista_filtrada = []

# 3. Recorremos cada elemento de la lista original
for item in lista_entrada:

    if item:
        lista_filtrada.append(item)

print(f"Lista original: {lista_entrada}")
print(f"Lista filtrada: {lista_filtrada}")