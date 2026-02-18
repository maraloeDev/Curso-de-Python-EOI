# ============================================================
# PARTE 2: EDICIÓN AVANZADA DE LISTAS (AÑADIR Y ELIMINAR)
# ============================================================

# --- 1. MÉTODOS PARA AÑADIR ELEMENTOS ---

# A) El método .append()
# Agrega un objeto como UN SOLO elemento al final.
list1 = [11, 22, 33, 44]
list1.append([55, 66])
print(f"Resultado con .append(): {list1}")
# Nota: La lista [55, 66] entra como un sub-elemento: [11, 22, 33, 44, [55, 66]]

# B) El método .extend()
# Agrega los elementos de una nueva lista de forma individual al final.
list2 = [11, 22, 33, 44]
list2.extend([55, 66])
print(f"Resultado con .extend(): {list2}")
# Nota: Se "fusionan": [11, 22, 33, 44, 55, 66]


# --- 2. MÉTODOS PARA ELIMINAR ELEMENTOS ---

# A) Palabra clave 'del'
# Borra el ítem en un índice específico (posición).
n_list = [11, 22, 33, 44, 55, 66]
del n_list[3] # Elimina el cuarto elemento (índice 3, que es el valor 44).
print(f"Después de 'del': {n_list}")

# B) Método .pop()
# Elimina y retorna el ÚLTIMO ítem de la lista.
# También puede borrar en una posición específica y devolver ese valor.
lista_pop = [10, 20, 30]
n = lista_pop.pop()
print(f"Valor extraído con .pop(): {n}") # Muestra 30
print(f"Lista tras .pop(): {lista_pop}") # Queda [10, 20]

# C) Método .remove()
# Elimina un elemento buscando su VALOR específico, no su índice.
lista_remove = [11, 22, 33, 44, 55, 66]
lista_remove.remove(44) # Busca el número 44 y lo quita.
print(f"Después de .remove(44): {lista_remove}")

# --- RESUMEN RÁPIDO ---
# - .append(): Añade un bloque entero.
# - .extend(): Añade contenido desglosado.
# - del: Borra por posición.
# - .pop(): Borra el último y te lo "da".
# - .remove(): Borra por nombre/valor.