import random

# ==========================================
# 1. TUPLAS Y COMPARACIONES (Imagen Q1)
# ==========================================
def leccion_tuplas():
    print("--- 1. Tuplas ---")
    # Las tuplas pueden definirse con o sin paréntesis
    t1 = 'a', 'b', 'c'
    t2 = ('a', 'b', 'c')
    t3 = ('d', 'e')

    # Las tuplas son iguales si tienen los mismos elementos
    print(f"t1 == t2: {t1 == t2}")  # True

    # Comparación lexicográfica (alfabética)
    # 'a' < 'd', por lo tanto t1 es menor que t3
    print(f"t1 > t3:  {t1 > t3}")   # False
    print(f"t1 < t3:  {t1 < t3}")   # True

    # Concatenación y listas que contienen tuplas
    print(f"Suma:     {t2 + t3}")   # ('a', 'b', 'c', 'd', 'e')
    print(f"En lista: {[t2 + t3]}") # [('a', 'b', 'c', 'd', 'e')]
    print("\n")

# ==========================================
# 2. LISTAS BIDIMENSIONALES (MATRICES)
# ==========================================
def leccion_matrices():
    print("--- 2. Matrices (Listas 2D) ---")
    # Una lista 2D es una lista de listas
    matriz = [
        [1, 2, 3], # Fila 0
        [4, 5, 6], # Fila 1
        [7, 8, 9]  # Fila 2
    ]

    # Acceso: lista[fila][columna]
    print(f"Elemento en fila 0, col 2: {matriz[0][2]}") # 3

    # Modificación de valores
    matriz[1][1] = 300
    print(f"Fila 1 modificada: {matriz[1]}") # [4, 300, 6]

    # Referencia vs Copia
    # Si asignas una lista a otra, ambas apuntan al mismo objeto
    copia_referencia = matriz
    copia_referencia[0][0] = 90
    print(f"El original también cambia: {matriz[0][0]}") # 90
    print("\n")

# ==========================================
# 3. LISTAS IRREGULARES (JAGGED LISTS)
# ==========================================
def leccion_jagged():
    print("--- 3. Listas Irregulares ---")
    # Son listas donde las filas tienen distintos tamaños
    # Se pueden crear con bucles anidados
    jagged = []
    for i in range(1, 6):
        fila = []
        for j in range(i):
            fila.append(j)
        jagged.append(fila)

    print("Estructura de la lista irregular:")
    for fila in jagged:
        print(fila)
    print("\n")

# ==========================================
# 4. CASO PRÁCTICO: RESERVA DE CINE
# ==========================================
def leccion_cine():
    print("--- 4. Aplicación: Cine ---")
    # Crear un mapa de asientos (3 filas x 6 columnas) con valores aleatorios
    asientos = []
    for i in range(3):
        fila = [random.randrange(0, 2) for _ in range(6)] # 0: Vacío, 1: Ocupado
        asientos.append(fila)

    # Contar asientos disponibles (valor 0)
    libres = 0
    for fila in asientos:
        print(" ".join(map(str, fila))) # Imprime la fila con formato
        for lugar in fila:
            if lugar == 0:
                libres += 1

    print(f"Asientos libres totales: {libres}")

# Ejecución de todas las lecciones
if __name__ == "__main__":
    leccion_tuplas()
    leccion_matrices()
    leccion_jagged()
    leccion_cine()