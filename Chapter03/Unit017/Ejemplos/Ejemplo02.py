### RESUMEN DE FUNCIONES INTEGRADAS (BUILT-IN FUNCTIONS) ###

# --- 1.3 & 1.4: Funciones Matemáticas Básicas ---
# No requieren importación previa.
print(f"Absoluto de -100: {abs(-100)}")          # abs(): Valor absoluto
print(f"Mínimo de la lista: {min(200, 100, 300)}") # min(): El valor más pequeño
print(f"Máximo de la lista: {max(200, 100, 300)}") # max(): El valor más grande

# --- 1.5: Ordenamiento (Sorting) ---
# sorted() devuelve una nueva lista ordenada.
letras = "EABFD"
numeros = [200, 100, 300, 480, 50]

print(f"String ordenado: {sorted(letras)}")              # Orden ascendente
print(f"Lista descendente: {sorted(numeros, reverse=True)}") # Orden descendente

# --- 1.6: Identidad y OOP ---
# id() devuelve el identificador único de un objeto en memoria.
a_str = "Hello Python!"
n = 300
print(f"ID de la cadena: {id(a_str)}")
print(f"ID del número: {id(n)}")

# --- 1.7: Tipos de Datos ---
# type() devuelve la clase o tipo de objeto.
print(f"Tipo de 123: {type(123)}")           # <class 'int'>
print(f"Tipo de 'Hola': {type('Hola')}")     # <class 'str'>
print(f"Tipo de 120.3: {type(120.3)}")       # <class 'float'>
print(f"Tipo de [1, 2]: {type([100, 300])}") # <class 'list'>

# --- 1.8: Evaluación de Strings y Unicode ---
# eval(): Ejecuta un string como si fuera código Python (¡Usar con precaución!)
print(f"Resultado de eval: {eval('10 + 20')}")

# len(): Devuelve la longitud (número de caracteres o elementos)
print(f"Longitud de 'FOO': {len('FOO')}")

# chr() y ord(): Conversión entre caracteres y valores Unicode
print(f"Unicode 65 es: {chr(65)}")    # De número a letra ('A')
print(f"Valor de 'A' es: {ord('A')}") # De letra a número (65)