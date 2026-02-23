"""
# Reto: El Limpiador de Datos de Inventario

# Contexto: Tienes una cadena de texto que contiene productos mal formateados, con espacios extra,

# errores de escritura y formatos de código inconsistentes. Tu misión es limpiar esta cadena usando

# los métodos del final de la Unidad 14.

"""

#RETO: LIMPIADOR DE INVENTARIO "ECO-SHOP"
#
#---------------------------------------
#
#OBJETIVO: Procesar y estandarizar una cadena de productos mal formateados.
#
#
#
#TAREAS A REALIZAR:
#
#1. LIMPIEZA: Eliminar espacios en blanco sobrantes (strip).
#
#2. CORRECCIÓN: Sustituir el texto "Error" por el código "003" (replace).
#
#3. NORMALIZACIÓN:
#
#- Nombre: Formato Capitalize (Ej: "Coke").
#
#4. FILTRADO: Mostrar por consola productos que empiecen por 'C' y terminen en '4'.
#
#5. EXPORTACIÓN: Unificar todo en un string separado por " - " (join).
#
#
#
#Entrada: "  cOFFee_001 ,  pEn_002 , milk_Error ,  coke_004 ,  bOOk_005 ,  PAPER cup_Error , suGar_007 ,  CHOCOlate_008 ,  cAnDY_009 , cHeeSe_010 ,  CARROT_014 ,  cookie_024 ,  cream_Error "
#
#Salida: "Coffee_001 - Pen_002 - Milk_003 - Coke_004 - Book_005 - Paper cup_003 - Sugar_007 - Chocolate_008 - Candy_009 - Cheese_010 - Carrot_014 - Cookie_024 - Cream_003"

"""

# 1. Datos de entrada

datos_sucios = "  cOFFee_001 ,  pEn_002 , milk_Error ,  coke_004 ,  bOOk_005 ,  PAPER cup_Error , suGar_007 ,  CHOCOlate_008 ,  cAnDY_009 , cHeeSe_010 ,  CARROT_014 ,  cookie_024 ,  cream_Error "
"""

datos_sucios = "  cOFFee_001 ,  pEn_002 , milk_Error ,  coke_004 ,  bOOk_005 ,  PAPER cup_Error , suGar_007 ,  CHOCOlate_008 ,  cAnDY_009 , cHeeSe_010 ,  CARROT_014 ,  cookie_024 ,  cream_Error "

# Separo la cadena por comas
lista_productos = datos_sucios.split(",")

productos_limpios = []

for producto in lista_productos:
    temp = producto.strip().replace("Error", "003")
    nombre_limpio = temp.capitalize()
    productos_limpios.append(nombre_limpio)

# 3. Filtrado: Productos que empiezan por 'C' y terminan en '4'
print("PRODUCTOS FILTRADOS (C...4)")
for p in productos_limpios:
    if p.startswith("C") and p.endswith("4"):
        print(f"Encontrado: {p}")


resultado_final = " - ".join(productos_limpios)


print("\n RESULTADO")
print(resultado_final)

