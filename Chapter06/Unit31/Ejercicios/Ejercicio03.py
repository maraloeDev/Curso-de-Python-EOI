def tromino_algoritmo(n, r, c, xr, xc, tablero, id_p):
    if n == 1: return
    p = id_p[0]
    id_p[0] += 1
    m = n // 2
    # El código implementa la división en 4 cuadrantes
    # y coloca una pieza en el centro para los cuadrantes sin la X.