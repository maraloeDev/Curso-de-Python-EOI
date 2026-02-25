"""
GUÍA DEFINITIVA SOBRE CLOSURES EN PYTHON
---------------------------------------
Definición: Una closure ocurre cuando una función interna (inner) hace referencia
a variables de su función externa (outer), y la función externa devuelve la
función interna.
"""

def definicion_closure():
    # 1. Función externa (Outer function)
    mensaje = "Hola desde el scope externo"

    def funcion_interna():
        # 2. La función interna accede a una variable 'no local'
        print(mensaje)

    # 3. Se devuelve la función interna sin ejecutarla ()
    return funcion_interna

# Uso básico
mi_closure = definicion_closure()
# Aunque 'definicion_closure' ya terminó, 'mi_closure' aún tiene acceso a 'mensaje'
mi_closure()


# --- EJEMPLOS COMUNES ---

### 1. Fábrica de Funciones (Multiplicadores)
# Este es el uso más clásico: crear funciones personalizadas sobre la marcha.

def fabricar_multiplicador(n):
    def multiplicador(x):
        return x * n
    return multiplicador

doblar = fabricar_multiplicador(2)
triplicar = fabricar_multiplicador(3)

print(f"Doble de 10: {doblar(10)}")    # Salida: 20
print(f"Triple de 10: {triplicar(10)}") # Salida: 30


### 2. Encapsulamiento de Datos (Estado Privado)
# Permite mantener un estado sin usar variables globales ni clases complejas.

def crear_contador():
    conteo = 0  # Esta variable está "protegida"

    def incrementar():
        nonlocal conteo  # Necesario para modificar la variable del scope superior
        conteo += 1
        return conteo

    return incrementar

contador_a = crear_contador()
print(f"Contador A: {contador_a()}") # 1
print(f"Contador A: {contador_a()}") # 2

contador_b = crear_contador() # Es una instancia independiente
print(f"Contador B: {contador_b()}") # 1


### 3. Reemplazo de Clases Simples
# Si solo necesitas un método y un estado, una closure es más ligera que una clase.

def setup_logger(nivel):
    def log(mensaje):
        print(f"[{nivel.upper()}]: {mensaje}")
    return log

log_error = setup_logger("error")
log_info = setup_logger("info")

log_error("Fallo en el sistema")
log_info("Usuario conectado")


# --- ¿CÓMO SABER SI ES UNA CLOSURE? ---
# Python guarda las variables capturadas en un atributo llamado __closure__
print(f"Celdas en la closure: {len(log_error.__closure__)}")
# El valor capturado ('error') está en la celda:
print(f"Valor capturado: {log_error.__closure__[0].cell_contents}")