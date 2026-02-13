print("#######################################"
          "\n"
          "Esta es la frutería de David."
          "\n"
          "1: Manzana (precio: 5000 won)"
          "\n"
          "2: Uva (precio: 6000 won)"
          "\n"
          "3: Melón (precio: 8000 won)"
          "\n"
          "4: Naranja (precio: 2000 won)"
          "\n"
          "#######################################")

opcion = int(input("Ingrese el número del artículo (entre 1 y 4) >> "))
cantidad = int(input("Ingrese la cantidad (entre 1 y 10) >> "))

nombre_fruta = ""
precio_unitario = 0

match opcion:
    case 1:
        nombre_fruta = "manzana"
        precio_unitario = 5000
    case 2:
        nombre_fruta = "uva"
        precio_unitario = 6000
    case 3:
        nombre_fruta = "melón"
        precio_unitario = 8000
    case 4:
        nombre_fruta = "naranja"
        precio_unitario = 2000
    case _:
        print("Opción no válida")
        exit()

total = precio_unitario * cantidad
print(f"Fruta seleccionada: {nombre_fruta}")
print(f"Precio: {precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"El precio total es {total} won.")

pago = int(input("Inserte dinero, por favor >>> "))

if pago >= total:
    cambio = pago - total
    print(f"{pago} won recibidos. Su cambio es {cambio} won.")
else:
    print("El dinero es insuficiente.")
