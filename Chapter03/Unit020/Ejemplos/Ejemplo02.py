"""
GUÍA MAESTRA: SCOPES Y CLOSURES EN PYTHON
Basado en los conceptos de la presentación:
1. LEGB Rule (Scopes)
2. First-Class Functions
3. Nested Functions
4. Closures & Nonlocal
"""

# --- 1. JERARQUÍA DE ÁMBITOS (REGLA LEGB) ---
#

# G: Global Scope (Nivel principal del script)
pais = "España"

def funcion_externa():
    # E: Enclosing Scope (Ámbito de la función superior)
    ciudad = "Madrid"

    def funcion_interna():
        # L: Local Scope (Ámbito dentro de la función propia)
        nombre = "Alex"

        # B: Built-in Scope (Funciones internas de Python como print() o len())
        print(f"{nombre} vive en {ciudad}, {pais}")

    funcion_interna()

# --- 2. FUNCIONES COMO OBJETOS DE PRIMER ORDEN ---
# Pueden ser asignadas a variables, pasadas y retornadas.

def multiplicar_por(n):
    # Esta es una "Nested Function" (Función anidada)
    def operacion(x):
        return x * n
    return operacion # Retornamos la función sin ejecutarla

# --- 3. CLOSURES (CLAUSURAS) ---
"""
Una Closure existe cuando:
1. Hay una función anidada.
2. La función anidada accede a una variable del ámbito 'Enclosing'.
3. La función externa retorna la función anidada.
"""

# Ejemplo: La función 'doblar' es una closure que "recuerda" que n=2
doblar = multiplicar_por(2)
# Aunque 'multiplicar_por' ya terminó de ejecutarse, 'n' vive en la closure.
print(f"Resultado de la closure: {doblar(10)}") # 20


# --- 4. LA PALABRA CLAVE 'NONLOCAL' ---
# Se usa para modificar variables del scope 'Enclosing' que no son globales.

def crear_acumulador(valor_inicial):
    total = valor_inicial # Variable en el Enclosing Scope

    def sumar(cantidad):
        nonlocal total # Sin esto, Python daría error al intentar reasignar 'total'
        total += cantidad
        return total

    return sumar

# --- PRUEBAS DE EJECUCIÓN ---

if __name__ == "__main__":
    print("--- 1. Prueba de Scopes ---")
    funcion_externa()

    print("\n--- 2. Prueba de Estado en Closure ---")
    cuenta_ahorro = crear_acumulador(100)
    print(f"Ingreso 50: {cuenta_ahorro(50)}")  # 150
    print(f"Ingreso 20: {cuenta_ahorro(20)}")  # 170

    print("\n--- 3. Inspección de la Closure ---")
    # Python guarda las variables capturadas en el atributo __closure__
    for celda in cuenta_ahorro.__closure__:
        print(f"Valor capturado en la 'mochila' de la función: {celda.cell_contents}")