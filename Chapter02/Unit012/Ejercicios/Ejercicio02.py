"""
En el ejemplo de salida que se muestra a continuación, hay tuplas que contienen elementos, así como también tuplas vacías,
cadenas de texto (strings) vacías y listas vacías que no tienen elementos.
Escribe un código para eliminar estas tuplas vacías, cadenas vacías y listas vacías de la lista proporcionada.
(Sin embargo, no elimines la tupla ((),) porque se considera que contiene una tupla vacía dentro)."
"""

lista_original = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']

lista_limpia = []

for elemento in lista_original:
    if elemento:
        lista_limpia.append(elemento)

print("Lista original:", lista_original)
print("Lista filtrada:", lista_limpia)