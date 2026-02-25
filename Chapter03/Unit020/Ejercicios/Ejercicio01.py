# --- EJERCICIO 1: EL SALUDADOR DINÁMICO (Scope Enclosing) ---
# Enunciado: Crea una función que fabrique saludos personalizados.
# La función externa recibe el "saludo" y la interna el "nombre".

def fabricar_saludo(prefijo):
    # 'prefijo' vive en el scope Enclosing
    def saludar(nombre):
        return f"{prefijo}, {nombre}"
    return saludar