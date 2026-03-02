def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        # Calculamos el punto medio
        medio = (bajo + alto) // 2
        valor_medio = lista[medio]

        print(f"Buscando entre índices {bajo} y {alto}. Punto medio: {medio} (Valor: {valor_medio})")

        if valor_medio == objetivo:
            return medio  # ¡Encontrado!
        elif valor_medio > objetivo:
            alto = medio - 1  # El objetivo está en la mitad izquierda
        else:
            bajo = medio + 1  # El objetivo está en la mitad derecha

    return -1  # No se encontró el elemento

# --- Pruebas del algoritmo ---
# La lista DEBE estar ordenada para que esto funcione
mi_lista = [11, 17, 26, 28, 37, 45, 53, 59]
numero_a_buscar = 53

print(f"Lista: {mi_lista}")
resultado = busqueda_binaria(mi_lista, numero_a_buscar)

if resultado != -1:
    print(f"\nÉxito: El número {numero_a_buscar} está en la posición {resultado}.")
else:
    print(f"\nEl número {numero_a_buscar} no se encuentra en la lista.")