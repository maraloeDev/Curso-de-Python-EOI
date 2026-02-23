"""
Tomemos un número n como entrada y encontremos la suma desde 1 hasta n. Escribe esta función utilizando una llamada de función recursiva.
"""
def fnumber(n):

    if n<= 1:
        return n
    else:
        return n - fnumber(n -1)


n = int(input("Introduce un numero: "))
print(fnumber(n = 10))
