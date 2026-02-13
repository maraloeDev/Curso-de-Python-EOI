"""
Unit 1: Sequential Programming
"""

#  Básico 1: Escribe un código que imprima "Hola Mundo" y en la siguiente línea
# "Aprendiendo Python".

print("Aprendiendo Python")

# Básico 2: Crea un programa que imprima tres frases distintas, cada una separada
# por una línea en blanco.
print(" Hola")
print(" Que tal")
print(" Estas")

# Medio 1: Diseña un algoritmo secuencial para calcular el volumen de un cubo
# pidiendo el lado por teclado.

lado = int(input("Introduce un  lado"))
print(f"El volumen de un cubo es {pow(lado,3)}")

# Medio 2: Crea un programa que pida el nombre de un producto y su precio, y luego
# imprima un recibo formateado

nombre_producto = str(input("Indique el nombre del producto: "))
precio_producto = str(input("Indique el precio del producto: "))
print("******************************************\n"
      f"Nombre del producto: {nombre_producto}"
      f"Precio del producto: {precio_producto}")