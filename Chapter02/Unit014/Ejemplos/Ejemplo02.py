# Definimos el diccionario inicial
dic = {'a': 10, 'b': 20, 'C': 30, 'd': 40}

# El método pop elimina la clave específica y devuelve su valor
# En este caso, elimina 'a' y devuelve 10
valor_eliminado = dic.pop('a')

print(f"Valor devuelto por pop: {valor_eliminado}")
print(f"Diccionario después de eliminar 'a': {dic}")

# Continuando con nuestro diccionario
dic = {'b': 20, 'C': 30}

# 1. keys(): Devuelve todas las llaves del diccionario
todas_las_llaves = dic.keys()
print(f"Llaves: {todas_las_llaves}") #

# 2. values(): Devuelve todos los valores del diccionario
todos_los_valores = dic.values()
print(f"Valores: {todos_los_valores}") #

# 3. items(): Devuelve los pares [llave]:[valor]
todos_los_items = dic.items()
print(f"Items: {todos_los_items}") #

# 4. get(key): Devuelve el valor de una llave; si no existe, devuelve None
# A diferencia de dic['llave'], get() no detiene el programa si la llave no existe
valor_b = dic.get('b')
valor_inexistente = dic.get('z')
print(f"Valor de 'b': {valor_b}, Valor de 'z': {valor_inexistente}") #

# 5. clear(): Elimina todos los elementos del diccionario
dic.clear()
print(f"Diccionario tras clear(): {dic}") #