"""
Python tiene el operador **, el cual indica una potencia.
Sin embargo, tomemos x y n como entradas sin usar un operador
 y utilicemos una función recursiva para obtener x elevado a la n-ésima potencia.
Intentemos obtener $2^{10}$ ingresando 2 como el valor de x y 10 como el valor de n de la siguiente manera:
"""

def potencia_recursiva(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia_recursiva(x, n - 1)

x = int(input("Enter x : "))
n = int(input("Enter n : "))


resultado = potencia_recursiva(x, n)
print(resultado)