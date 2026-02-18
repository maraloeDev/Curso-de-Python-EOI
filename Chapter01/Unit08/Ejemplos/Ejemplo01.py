"""
Código final de Combinaciones de Comida Deliciosa

El código muestra listas de panes, carnes, vegetales y salsas.

Utiliza bucles anidados (for) para recorrer cada lista y generar todas las combinaciones posibles de sándwiches para la tienda de David.

El resultado final imprime cada combinación uniendo los ingredientes con espacios.
"""

breads = ["Rye bread", "Wheat", "White"]
meats = ["Meatball", "Sausage", "Chicken breast"]
vegis = ["Lettuce", "Tomato", "Cucumber"]
sauces = ["Mayonnaise", "Honey Mustard", "Chili"]

print("Possible combinations of David's sandwich shop:")

# Los 4 bucles anidados recorren todas las listas
for b in breads:
    for m in meats:
        for v in vegis:
            for s in sauces:
                # Se imprimen todos los ingredientes unidos por espacios
                print(b + " " + m + " " + v + " " + s)