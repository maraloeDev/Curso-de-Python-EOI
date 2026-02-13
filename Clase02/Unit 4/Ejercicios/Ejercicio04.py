# Crear una tabla con los numeros cuadrados del 2 al 6 en una tabla
# Definimos el exponente fijo n
n = 2
# Imprimimos el encabezado de la tabla (usamos espacios para alinear)
print("a    n    a ** n")
# Paso 1: a vale 2
a = 2
print(a, "  ", n, "  ", a ** n)
# Paso 2: a vale 3
a = 3
print(a, "  ", n, "  ", a ** n)
# Paso 3: a vale 4
a = 4
print(a, "  ", n, "  ", a ** n)
# Paso 4: a vale 5
a = 5
print(a, "  ", n, "  ", a ** n)
# Paso 5: a vale 6
a = 6

print(a, "  ", n, "  ", a ** n)

print("a    n    a ** n")

# Bucle en un rango de 2 (a) a 6 (inclusive): el rango en Python es exclusivo, por eso ponemos 7


for a in range(n, 7):
    print(a, "  ", n, "  ", a ** n)
