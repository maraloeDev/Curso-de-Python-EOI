def ejercicio06_8x8():
    N = 8
    tablero = [[0]*N for _ in range(N)]
    # X en posición (6,5) según la imagen 8x8
    tablero[6][5] = -1
    return tablero