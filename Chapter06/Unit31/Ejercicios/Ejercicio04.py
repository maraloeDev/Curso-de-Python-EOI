def colocar_tromino(tablero, n, r, c, hr, hc, id_p):
    if n == 2:
        for i in range(r, r + 2):
            for j in range(c, c + 2):
                if not (i == hr and j == hc):
                    tablero[i][j] = id_p[0]
        id_p[0] += 1
        return
    # Recursividad para tamaños mayores...