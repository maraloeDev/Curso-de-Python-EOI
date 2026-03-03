def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    # Paso 2: Si no miden lo mismo
    if len(palabra1) != len(palabra2):
        return False

    # Paso 3: Crear un diccionario para almacenar cada letra
    conteo = {}

    # Sumamos las letras de la primera palabra, si se encuentra la pala
    for letra in palabra1:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1

    # Restamos las letras de la segunda palabra
    for letra in palabra2:
        if letra in conteo:
            conteo[letra] -= 1
        else:
            # Si hay una letra en palabra2 que no estaba en palabra1
            return False

    # Paso 4: Si todas las cuentas llegaron a cero, es un anagrama
    for valor in conteo.values():
        if valor != 0:
            return False

    return True

# Prueba
p1 = "LISTEN"
p2 = "SILENT"
print(f"¿Son anagramas? {es_anagrama(p1, p2)}")