# No necesitas importar nada para usar booleanos básicos

numero = int(input("Introduce un numero: "))
mi_bool = True

if 0 < numero < 10:  # Python permite simplificar rangos así
    print(not mi_bool)  # Usamos 'not' en lugar de '!'
else:
    print(mi_bool)