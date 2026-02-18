import random

# =========================================================
# 1. TRABAJANDO CON TUPLAS (Basado en Q1 y Q2)
# =========================================================
print("--- SECCIÓN 1: TUPLAS ---")

# Las tuplas pueden definirse sin paréntesis (empaquetado)
t1 = 'a', 'b', 'c'
t2 = ('a', 'b', 'c')
t3 = ('d', 'e')

# Comparación: se hace elemento por elemento
print(f"¿Es t1 igual a t2?: {t1 == t2}")  # True
print(f"¿Es t1 menor que t3?: {t1 < t3}")   # True, porque 'a' viene antes que 'd'

# Ejercicio de Ventas (Q2): Comparar valores actuales con el anterior
ventas = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
dias_baja = 0
for i in range(1, len(ventas)):
    if ventas[i] < ventas[i-1]:  # Si hoy vendí menos que ayer
        dias_baja += 1
print(f"Días con ventas reducidas: {dias_baja}")
print("-" * 30)


# =========================================================
# 2. LISTAS BIDIMENSIONALES (Matrices) (Basado en 1.1 y 2.1)
# =========================================================
print("\n--- SECCIÓN 2: LISTAS 2D (MATRICES) ---")

# Crear una matriz 4x4 manualmente
# Cada sub-lista es una FILA
matriz = [
    [1, 2, 3, 4],    # Fila 0
    [5, 6, 7, 8],    # Fila 1
    [9, 10, 11, 12], # Fila 2
    [13, 14, 15, 16] # Fila 3
]

# Acceso: matriz[fila][columna]
print(f"Elemento en Fila 1, Col 2: {matriz[1][2]}") # Resultado: 7

# Modificar un valor (Asignación)
matriz[2][1] = 100
print(f"Fila 2 actualizada: {matriz[2]}") # [9, 100, 11, 12]
print("-" * 30)


# =========================================================
# 3. EL CINE (Uso de matrices y bucles) (Basado en Mission 2.1)
# =========================================================
print("\n--- SECCIÓN 3: SISTEMA DE CINE ---")

# Crear un cine de 3 filas x 6 columnas con asientos aleatorios
cine = []
for f in range(3):
    fila = []
    for c in range(6):
        # 0 = Vacío, 1 = Ocupado
        asiento = random.randrange(0, 2)
        fila.append(asiento)
    cine.append(fila)

# Mostrar el mapa del cine y contar vacíos
asientos_libres = 0
print("Mapa de asientos (0=Libre, 1=Ocupado):")
for fila in cine:
    print(fila) # Imprime cada fila
    for asiento in fila:
        if asiento == 0:
            asientos_libres += 1

print(f"Total de asientos disponibles: {asientos_libres}")