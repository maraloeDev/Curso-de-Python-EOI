"""
Crea el diccionario fruits_dic que tenga los siguientes elementos de clave-valor.
Luego, utiliza este diccionario para imprimir el precio de cada fruta como se muestra a continuación."
"""

fruits_dic = {
    "apple": 5000,
    "banana": 4000,
    "grape": 5300,
    "melon": 6500
}

for fruit, price in fruits_dic.items():
    print(f"The price of a {fruit} is {price} KRW.")