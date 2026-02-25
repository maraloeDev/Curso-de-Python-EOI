"""
El número natural $e$, también llamado número de Euler o constante de Napier,
es un número irracional utilizado como base del logaritmo natural.
a, sea $k!$ definido como una función llamada factorial(k). Además, definamos una función llamada euler(n) que devuelva
la suma de $1/0! + 1/1!$ hasta $1/n!$.Encuentra el valor de euler(20) con cinco decimales y
muéstralo de la siguiente manera. (Debes usar una función recursiva).
"""

def factorial(k):
    if k == 0:
        return 1
    else:
        return k * factorial(k - 1)

def euler(n):
    if n == 0:
        return 1 / factorial(0)
    # Caso recursivo: suma el término actual (1/n!) a los anteriores
    else:
        return (1 / factorial(n)) + euler(n - 1)

# Cálculo del resultado
resultado = euler(20)

#(5 decimales)
print(f"euler(20) = {resultado:.5f}")