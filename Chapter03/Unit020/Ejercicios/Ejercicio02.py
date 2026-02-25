# --- EJERCICIO 2: EL CONTADOR PRIVADO (Uso de Nonlocal) ---
# Enunciado: Crea una closure que funcione como un contador.
# Debe incrementar un valor interno cada vez que se llama.
# Concepto clave: 'nonlocal' (imagen image_2497fd.png)

def crear_contador():
    cuenta = 0  # Variable local de la función externa

    def incrementar():
        nonlocal cuenta  # Permite modificar la variable del nivel superior
        cuenta += 1
        return cuenta

    return incrementar