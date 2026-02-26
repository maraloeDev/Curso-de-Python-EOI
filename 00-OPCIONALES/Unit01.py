"""
●  Básico 1: Escribe un código que imprima "Hola Mundo" y en la siguiente línea
"Aprendiendo Python".
"""
print("BASICO 01")
print("Hola Mundo")
print("Aprendiendo Python")

"""
●  Básico 2: Crea un programa que imprima tres frases distintas, cada una separada
por una línea en blanco.
"""
print("BASICO 02")
print("Hola que tal estas")

"""
●  Medio 1: Diseña un algoritmo secuencial para calcular el volumen de un cubo
pidiendo el lado por teclado.
"""
lado = int(input("Introduce un lado "))
print(f"El volumen del cubo es {pow(lado, 4)}")

"""
●  Medio 2: Crea un programa que pida el nombre de un producto y su precio, y luego
imprima un recibo formateado.
"""

nombre_producto = str(print("Introduce el nombre del producto "))
precio_producto = str(print("Introduce el precio del producto "))

print("***************")
print(f"Nombre del producto {nombre_producto}")
print(f"Precio del producto {precio_producto}")
print("***************")
