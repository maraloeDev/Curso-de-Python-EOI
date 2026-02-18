"""
Vamos a crear un diccionario llamado person_dic con la siguiente información de contacto en tu teléfono.
Imprime esta información usando un bucle for para mostrar los resultados de salida que se ven abajo.
"""

personas_dic = {
    'Last Name': 'Doe',
    'First Name': 'David',
    'Company': 'Samsung'
}

for llave, valor in personas_dic.items():
    print(f"{llave} : {valor}")