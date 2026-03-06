"""
TEMA: FUNDAMENTOS Y PASOS DEL ENFOQUE CODICIOSO (GREEDY APPROACH)
---------------------------------------------------------------
DEFINICIÓN:
Es una técnica de diseño de algoritmos que llega a una solución
seleccionando la "mejor" opción en el momento actual según criterios
predefinidos.

Es una técnica muy eficiente y simple para resolver problemas de
optimización.
"""

def explicar_pasos_greedy():
    """
    Según la Unidad 30 (Sección 1.1), el enfoque codicioso
    resuelve los problemas en tres pasos críticos:
    """

    pasos = {
        "1. Proceso de Selección":
            "Elegir el siguiente elemento para añadir al conjunto de soluciones.",

        "2. Verificación de Factibilidad":
            "Comprobar si el nuevo conjunto es apropiado para ser la respuesta.",

        "3. Verificación de la Solución":
            "Determinar si el nuevo conjunto resuelve el problema por completo."
    }

    for paso, descripcion in pasos.items():
        print(f"{paso}: {descripcion}")

# ==========================================================
# EJEMPLO DETALLADO: CAMBIO DE 870 WON (Lógica de la diapositiva)
# ==========================================================
# Las monedas disponibles en Corea son: 500, 100, 50, 10

def simulacion_greedy_870():
    monto = 870
    monedas_disponibles = [500, 100, 50, 10] #
    seleccion = []

    print(f"Cambio inicial: {monto} won")

    # Paso 1: Selección de la moneda más grande (500)
    monto -= 500
    seleccion.append(500)
    print(f"Seleccionada: 500 won. Restante: {monto} won") # Restan 370

    # Paso 2: Como 500 ya no cabe, se elige la siguiente más grande (100)
    monto -= 100
    seleccion.append(100)
    print(f"Seleccionada: 100 won. Restante: {monto} won") # Restan 270

    # Paso 3: Se elige otra de 100 porque sigue siendo factible
    monto -= 100
    seleccion.append(100)
    print(f"Seleccionada: 100 won. Restante: {monto} won") # Restan 170

    return seleccion

# --- Ejecución de la teoría ---
if __name__ == "__main__":
    print("--- PASOS DEL ENFOQUE CODICIOSO ---")
    explicar_pasos_greedy()
    print("\n--- SIMULACIÓN VISUAL (870 WON) ---")
    resultado = simulacion_greedy_870()
    print(f"\nResultado final: {resultado}") # [500, 100, 100, 100, 50, 10, 10]