# ============================================================
# GUÍA PRÁCTICA DE MÉTODOS DE LISTAS (ADICIÓN Y ELIMINACIÓN)
# ============================================================

# --- 1. MÉTODOS DE ADICIÓN Y EXPANSIÓN ---

# A) El método .append()
# Agrega el objeto tal cual al final de la lista.
list1 = [11, 22, 33, 44]
list1.append([55, 66])
print(f"Resultado de .append([55, 66]): {list1}")
# Nota: Crea una lista anidada (una lista dentro de otra).

# B) El método .extend()
# Añade los elementos de una nueva lista individualmente.
list2 = [11, 22, 33, 44]
list2.extend([55, 66])
print(f"Resultado de .extend([55, 66]): {list2}")
# Nota: Los elementos se "fusionan" en una sola lista plana.


# --- 2. MÉTODOS DE ELIMINACIÓN ---

# A) Palabra clave 'del'
# Elimina un elemento usando su índice (posición).
n_list_del = [11, 22, 33, 44, 55, 66]
del n_list_del[3] # Elimina el elemento en la posición 3 (el valor 44).
print(f"Después de 'del n_list[3]': {n_list_del}")

# B) Método .pop()
# Elimina el último elemento y lo devuelve (retorna).
n_list_pop = [10, 20, 30]
item_sacado = n_list_pop.pop()
print(f"Elemento extraído con .pop(): {item_sacado}") # Muestra 30.
print(f"Lista después de .pop(): {n_list_pop}")    # Muestra [10, 20].

# C) Método .remove()
# Elimina un elemento buscando su VALOR específico.
n_list_rem = [11, 22, 33, 44, 55, 66]
n_list_rem.remove(44) # Busca el número 44 y lo borra.
print(f"Después de .remove(44): {n_list_rem}")


# --- RESUMEN DE DIFERENCIAS ---
# - append vs extend: Uno mete la "caja" entera, el otro vacía el contenido.
# - del vs remove: 'del' usa la posición (índice), 'remove' usa el nombre (valor).
# - pop: Es el único que te entrega el valor que acaba de borrar.