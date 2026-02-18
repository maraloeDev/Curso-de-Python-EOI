"""
Vamos a mejorar el programa para gestionar el inventario de tiendas de conveniencia que resolvimos anteriormente.
En otras palabras, añade código para aumentar o disminuir el inventario.
Además, crea un menú sencillo que incluya: consulta de inventario, entrada de mercancía
(almacenamiento) y salida de mercancía (envío).
"""

items = {"Coffee": 7, "Pen": 3, "Papercio cup": 2, "Milk": 1, "Coke": 4, "Book": 5}

while True:
    print("\nSeleccione menú ""1) consultar stock 2) entrada 3) salida 4) salir :", end=" ")
    menu = input()

    if menu == '1':

        articulo = input("[Consulta de stock] Ingrese artículo: ")

        print(f"Stock: {items.get(articulo, 0)}")

    elif menu == '2':
        entrada = input("[Entrada] Ingrese artículo y cantidad: ").split()
        nombre, cantidad = entrada[0], int(entrada[1])

        items[nombre] = items.get(nombre, 0) + cantidad
        print(f"Nuevo stock de {nombre}: {items[nombre]}")

    elif menu == '3':
        entrada = input("[Salida] Ingrese artículo y cantidad: ").split()
        nombre, cantidad = entrada[0], int(entrada[1])

        if nombre in items:
            items[nombre] -= cantidad
        else:
            print("El artículo no existe en el inventario.")

    elif menu == '4':
        print("Programa finalizado.")
        break