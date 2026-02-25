"""
Este ejercicio pide que el usuario introduzca tres números y
el programa calcule tres estadísticas diferentes usando funciones específicas.
"""
def mean3(a, b, c):
    return (a + b + c) / 3

def max3(a, b, c):
    return max(a, b, c)

def min3(a, b, c):
    return min(a, b, c)

# Entrada de usuario
# El ejemplo muestra "9 2 6", así que usamos split() para leerlos en una línea
entrada = input("Enter three numbers : ")
a, b, c = map(int, entrada.split())

# Resultados
print(f"The average value of {a}, {b}, {c} is {mean3(a, b, c)}")
print(f"The maximum value of {a}, {b}, {c} is {max3(a, b, c)}")
print(f"The minimum value of {a}, {b}, {c} is {min3(a, b, c)}")