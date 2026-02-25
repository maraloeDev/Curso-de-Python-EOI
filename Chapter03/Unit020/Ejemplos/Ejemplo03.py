"""
PARTE FINAL: PERSISTENCIA Y ESTADO EN CLOSURES
Conceptos: Memory management, data persistence y el objeto __closure__.
"""

# --- 1. PERSISTENCIA DE DATOS (Data Persistence) ---
# Según tus diapositivas, una closure permite que los datos "sobrevivan"
# a la ejecución de la función externa.

def crear_servidor(nombre_app):
    """
    La variable 'nombre_app' queda atrapada en el entorno de la closure.

    """
    estado = "Offline" # Variable de estado interna

    def cambiar_estado(nuevo_estado):
        nonlocal estado
        estado = nuevo_estado
        return f"Servidor {nombre_app} está ahora: {estado}"

    return cambiar_estado

# Instanciamos dos "servidores" independientes
app_web = crear_servidor("E-Commerce")
app_api = crear_servidor("API-Rest")

print(app_web("Online"))   # El nombre "E-Commerce" persiste
print(app_api("Mantenimiento")) # Cada closure tiene su propia "mochila" de datos


# --- 2. EL OBJETO __closure__ (Bajo el capó) ---
# Python almacena las variables capturadas en una estructura interna.

def funcion_externa(valor):
    def funcion_interna():
        return valor * 2
    return funcion_interna

mi_clausura = funcion_externa(50)

# ¿Cómo sabe 'mi_clausura' que el valor era 50?
# Accedemos a las 'cells' (celdas) de la closure:
if mi_clausura.__closure__:
    valor_guardado = mi_clausura.__closure__[0].cell_contents
    print(f"\nValor recuperado de la memoria interna: {valor_guardado}")


# --- 3. RECAPITULACIÓN TRADUCIDA (Basado en las imágenes) ---

resumen = {
    "Nested Function": "Función definida dentro de otra.",
    "First-Class Objects": "Funciones que se tratan como datos (se pueden retornar).",
    "Encapsulamiento": "Ocultar variables para que no sean accesibles desde fuera.",
    "Persistencia": "Capacidad de recordar valores tras finalizar la función padre."
}

def mostrar_resumen():
    print("\n--- RESUMEN CONCEPTUAL ---")
    for concepto, definicion in resumen.items():
        print(f"{concepto}: {definicion}")

# --- 4. EJERCICIO FINAL: EL GENERADOR DE FILTROS ---
# Crea una closure que reciba un umbral y filtre una lista de números.

def fabricar_filtro(umbral):
    def filtrar(lista):
        # La closure recuerda el 'umbral'
        return [n for n in lista if n > umbral]
    return filtrar

filtro_mayores_10 = fabricar_filtro(10)
numeros = [2, 15, 8, 20, 3, 11]

print(f"\nNúmeros mayores a 10: {filtro_mayores_10(numeros)}")


if __name__ == "__main__":
    mostrar_resumen()