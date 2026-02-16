"""
Desarrolla un programa de pedidos de menú para el restaurante "Yummy Restaurant".
Muestra el siguiente menú al usuario y permite que elija una opción.
 Si la letra ingresada no está en el menú, imprime: "Enter the menu again: "
 (Ingresa el menú de nuevo) y recibe otra entrada.
"""
print("Bienvenido a Yummy Restaurant. Aquí está el menú.")
print("- Hamburguesa (ingresa b)")
print("- Pollo (ingresa c)")
print("- Pizza (ingresa p)")

while True:
    opcion = input("Elige un menú (ingresa b, c, p): ").lower()

    if opcion == 'b' or opcion == 'c' or opcion == 'p':
        break
    else:
        print("Ingresa el menú de nuevo: ", end="")

if opcion == 'b':
    print("Elegiste hamburguesa.")
elif opcion == 'c':
    print("Elegiste pollo.")
elif opcion == 'p':
    print("Elegiste pizza.")