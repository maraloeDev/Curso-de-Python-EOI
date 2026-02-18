"""
Crea el diccionario fruits_dic que consista en los pares clave-valor incluyendo
('apple', 6000), ('melon', 3000), ('banana', 5000), ('orange', 4000).
Luego, imprime todas las claves de fruits_dic como tipo lista y examina si las claves 'apple' y 'mango'
se encuentran en fruits_dic, e imprime los resultados como se muestra a continuación."
"""

# Creo el diccionario frutas
fruits_dic = {
    'apple': 6000,
    'melon': 3000,
    'banana': 5000,
    'orange': 4000
}

# Muestro por consola solo las keys
print(fruits_dic.keys())

# 3 Compruebo si apple esta en el diccionario lo imprimo, si no, muestro un mensaje por consola
if 'apple' in fruits_dic:
    print("apple is in fruits_dic.")
else:
    print("apple is not in fruits_dic.")

# 4. Examinar si 'mango' se encuentra en el diccionario
if 'mango' in fruits_dic:
    print("mango is in fruits_dic.")
else:
    print("mango is not in fruits_dic.")