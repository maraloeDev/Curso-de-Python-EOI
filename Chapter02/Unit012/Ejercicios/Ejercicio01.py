"""
Retorna el elemento que tenga el número máximo de ocurrencias (el que más veces se repita).
 Cuando haya más de dos elementos con la misma frecuencia máxima, imprime el número más alto.
"""

nums = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)


repeticiones = 0  # Veces que se repite un número
numero_mas_frecuente = 0 # Guardará el valor del número que más veces aparece

# Recorro cada "item"
for i in nums:
    # Cuento cuántas veces aparece el número 'i'
    conteo_actual = nums.count(i)

    # Si el numero actual es mayor que nuestra referencia guardada
    if conteo_actual > repeticiones:
        # Actualizamos la frecuencia máxima y el número ganador
        frecuencia_maxima = conteo_actual
        numero_mas_frecuente = i

    elif conteo_actual == repeticiones:
        # Comparamos los valores para imprimir el número más alto
        if i > numero_mas_frecuente:
            numero_mas_frecuente = i

print(f"El elemento más frecuente es: {numero_mas_frecuente}")