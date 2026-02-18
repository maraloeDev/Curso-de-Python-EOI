# RESUMEN DE CONCEPTOS: TUPLAS Y LISTAS BIDIMENSIONALES

# --- 1. TUPLAS Y COMPARACIONES (Imagen Q1) ---
# Las tuplas se pueden definir con o sin paréntesis.
t1 = 'a', 'b', 'c'  # Empaquetado automático
t2 = ('a', 'b', 'c')
t3 = ('d', 'e')

print("--- 1. Tuplas ---")
print(t1 == t2)       # True: Tienen el mismo contenido
print(t1 < t3)        # True: 'a' es menor que 'd' en orden alfabético
print(t2 + t3)        # ('a', 'b', 'c', 'd', 'e'): Concatenación
print([t2 + t3])      # [('a', 'b', 'c', 'd', 'e')]: Una lista que contiene una tupla


# --- 2. ITERACIÓN CON TUPLAS (Imagen Q2) ---
ventas = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
reducidas = 0

for i in range(1, len(ventas)):
    if ventas[i] < ventas[i-1]: # Compara día actual con el anterior
        reducidas += 1
print(f"\n--- 2. Ventas reducidas: {reducidas} días ---")


# --- 3. LISTAS BIDIMENSIONALES (MATRICES) (Imágenes 1.1 a 2.2) ---
# Una lista 2D es una lista que contiene otras listas.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n--- 3. Listas 2D ---")
print(f"Fila 0 completa: {matriz[0]}")     # Acceso a una fila
print(f"Elemento específico: {matriz[0][2]}") # Fila 0, Columna 2 -> 3

# Modificar elementos
matriz[1][1] = 300 # Cambia el 5 por 300
print(f"Matriz modificada: {matriz[1]}")


# --- 4. BUCLES ANIDADOS Y MATRICES (Imagen Mission 2.1) ---
# Ejemplo práctico: Sistema de asientos de cine (3 filas x 6 columnas)
import random

cine = []
for f in range(3):
    fila = []
    for c in range(6):
        fila.append(random.randrange(0, 2)) # 0: Vacío, 1: Ocupado
    cine.append(fila)

# Contar asientos disponibles (0)
disponibles = 0
print("\n--- 4. Mapa del Cine ---")
for fila in cine:
    print(fila)
    for asiento in fila:
        if asiento == 0:
            disponibles += 1

print(f"Asientos libres totales: {disponibles}")