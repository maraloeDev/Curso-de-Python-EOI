print("\n--- Operaciones de Secuencias ---")

# 2.1 Indexación (Acceso por posición)
# En Python, el primer elemento es siempre el índice 0.
lista_indices = [11, 22, 33, 44, 55, 66]
print(f"Lista original: {lista_indices}")
print(f"Elemento en índice 0: {lista_indices[0]}") # 11
print(f"Elemento en índice 2: {lista_indices[2]}") # 33

# 2.2 Índices Negativos (Desde el final)
# El índice -1 es el último elemento, -2 el penúltimo, etc.
print(f"Último elemento (índice -1): {lista_indices[-1]}") # 66

# 2.3 El método .index()
# Devuelve la posición de la primera aparición de un valor.
lista_busqueda = [10, 20, 30, 40]
posicion = lista_busqueda.index(10)
print(f"El valor 10 está en la posición: {posicion}") # 0

# 2.4 Operadores de membresía (in / not in)
# Devuelven True o False si el elemento existe.
print(f"¿Está el 10 en la lista?: {10 in lista_busqueda}") # True

# 2.5 Vincular (Concatenar) objetos (+)
# Se unen secuencias del mismo tipo.
list1 = [1, 2, 3]
list2 = [4, 5]
print(f"Listas vinculadas: {list1 + list2}") #

# 2.6 Iteración / Repetición (*)
# Repite los elementos de una secuencia N veces.
print(f"String repetido: {'Hola' * 3}") #

# Para repetir un range, hay que convertirlo primero.
ran_repetido = list(range(3)) * 2
print(f"Range convertido y repetido: {ran_repetido}") #

# 2.7 Método .count()
# Cuenta cuántas veces aparece un elemento específico.
lista_conteo = [11, 11, 22, 33]
print(f"Veces que aparece el 11: {lista_conteo.count(11)}") # 2