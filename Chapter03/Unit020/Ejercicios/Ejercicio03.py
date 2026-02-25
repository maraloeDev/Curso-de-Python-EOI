# --- EJERCICIO 3: CALCULADORA DE POTENCIAS (Closure con Argumentos) ---
# Enunciado: Implementa una fábrica de potencias (cuadrados, cubos, etc.)
# utilizando funciones de primer orden.

def elevar_a(exponente):
    def calcular(base):
        return base ** exponente
    return calcular