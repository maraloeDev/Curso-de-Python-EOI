"""
Queremos convertir el valor de millas, la unidad utilizada principalmente en los
Estados Unidos,al valor de kilómetros, la unidad estándar internacional.
Implementa la función mile2km(mi) que tome un valor en millas como parámetro y lo devuelva en kilómetros.
Llama a esta función para mostrar de 1 a 5 millas en kilómetros;
en este caso, utiliza for _ in range para hacerlo repetitivo. (Define 1 milla como 1.61 km).
"""

def mile2km(mi):
    return mi * 1.61

for i in range(1, 6):

    km = mile2km(i)
    print(f"{i} millas son {km:.2f} kilómetros")