"""
Vamos a escribir un programa que realice la gestión de inventario de una tienda de conveniencia.
Para ello, el inventario de los artículos vendidos se almacena en el diccionario items como se muestra en el ejemplo de abajo.
Escribe un programa que reciba el nombre del artículo por parte de los usuarios y devuelva el inventario de dicho artículo.
Supón que es una tienda muy pequeña y los artículos tratados son los siguientes.
"""

items = {
    'Milk': 1,
    'Bread': 5,
    'Eggs': 12,
    'Coffee': 10
}

articulo = input("Enter name of the item: ")
res = items.get(articulo, "No disponible")
print(res)

