"""
Implementa la función max2(m, n), la cual toma dos parámetros llamados m y n, y devuelve el mayor de estos dos valores,
y la función min2(m, n) que también toma dos parámetros llamados m y n y devuelve el menor de estos dos valores.
Asigna 100 y 200 como argumentos y llama a ambas funciones para comprobar los resultados.
"""

def max2(m, n):
    if m > n:
        return m
    else:
        return n

def min2(m, n):
    if m < n:
        return m
    else:
        return n

# Comprobación de resultados
print("The greater of 100 or 200 is :", max2(100, 200))
print("The smaller of 100 or 200 is :", min2(100, 200))