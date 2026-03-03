""""
Utilizando la lista [50, 30, 40, 10, 20], aplica el método de Inserción para
organizar los elementos, simulando el desplazamiento de objetos para hacer espacio.
"""

def ejercicio2_insercion(lista):
    # Comenzamos desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        j = i - 1

        # Desplazamos los elementos de la izquierda que sean mayores al valor_actual
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j] # Desplazamiento (Shift)
            j -= 1

        # Insertamos el valor en su posición correcta
        lista[j + 1] = valor_actual
    return lista

# Datos de prueba
canicas = [50, 30, 40, 10, 20]
print("\n--- EJERCICIO 2 ---")
print(f"Resultado Inserción: {ejercicio2_insercion(canicas)}")