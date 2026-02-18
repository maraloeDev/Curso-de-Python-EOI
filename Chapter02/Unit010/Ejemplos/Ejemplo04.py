# ============================================================
# RESUMEN COMPLETO: MANIPULACIÓN Y MODIFICACIÓN DE LISTAS
# ============================================================

# --- 1. MÉTODOS DE EXPANSIÓN (ADICIÓN) ---

# A) El método .append()
# Agrega un objeto ÚNICO al final. Si pasas una lista, la mete entera como un sub-elemento.
list_a = [11, 22, 33, 44]
list_a.append([55, 66])
# Resultado: [11, 22, 33, 44, [55, 66]]

# B) El método .extend()
# Agrega los elementos de una nueva lista uno por uno al final de la original.
list_b = [11, 22, 33, 44]
list_b.extend([55, 66])
# Resultado: [11, 22, 33, 44, 55, 66]


# --- 2. MÉTODOS DE ELIMINACIÓN ---

n_list = [11, 22, 33, 44, 55, 66]

# A) Palabra clave 'del'
# Borra el ítem en un índice específico. No se puede usar con el valor directamente (ej: del 44 no funciona).
del n_list[3] # Elimina el elemento en el índice 3 (el número 44)
# n_list ahora es: [11, 22, 33, 55, 66]

# B) Método .pop()
# Elimina el ÚLTIMO ítem de la lista y, al mismo tiempo, te lo devuelve para que lo uses.
lista_pop = [10, 20, 30]
valor_sacado = lista_pop.pop()
# valor_sacado = 30, lista_pop = [10, 20]

# C) Método .remove()
# Borra un elemento buscando su VALOR exacto, no su posición.
lista_remove = [11, 22, 33, 44, 55, 66]
lista_remove.remove(44) # Busca el 44 y lo elimina
# Resultado: [11, 22, 33, 55, 66]


# --- 3. CONCEPTOS DE ÍNDICES Y LONGITUD ---

# len() nos da el número total de elementos.
# El índice negativo -1 siempre apunta al último elemento.
items = [10, 20, 30, 40]
print(len(items))    # Salida: 4
print(items[-1])     # Salida: 40

# ------------------------------------------------------------
# Resumen de herramientas:
# - Para añadir: .append() (uno), .extend() (muchos), + (unir).
# - Para borrar: del (por índice), .pop() (el último), .remove() (por valor).