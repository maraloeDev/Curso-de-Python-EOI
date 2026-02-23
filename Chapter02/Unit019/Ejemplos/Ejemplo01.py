# =================================================================
# GUÍA DE ESTUDIO: LAMBDAS, ITERADORES Y EXCEPCIONES
# =================================================================

"""
1. DEFINICIÓN: EXPRESIONES LAMBDA
Son funciones anónimas de una sola línea. Se usan para crear lógica rápida
sin necesidad de definir una función formal con 'def'.
Sintaxis: lambda parámetros : expresión.
"""

# Ejemplo de Lambda (Suma simple)
add = lambda x, y: x + y
print(f"Suma Lambda: {add(100, 200)}") # Resultado: 300

# Ejemplo de Lambda Inmediata (IIFE)
# Se define y se ejecuta en la misma línea.
print(f"Suma Inmediata: {(lambda x, y: x + y)(100, 200)}")


"""
2. DEFINICIÓN: FUNCIONES FILTER Y MAP
- FILTER: Recibe un iterable y devuelve solo los elementos que cumplen 
  una condición (donde la función retorna True).
- MAP: Aplica una función a cada elemento de un iterable para transformarlo.
"""

# Ejercicio Q2: Filtrar números pares
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x % 2 == 0, n_list))
print(f"Lista de pares: {even_list}")

# Ejercicio Q3: Convertir a mayúsculas con MAP
a_list = ['a', 'b', 'c', 'd']
upper_a_list = list(map(lambda x: x.upper(), a_list))
print(f"Lista Mayúsculas: {upper_a_list}")


"""
3. DEFINICIÓN: MANEJO DE EXCEPCIONES (TRY-EXCEPT)
Es una estructura para prevenir que el programa se detenga por errores inesperados.
- try: Código que puede fallar.
- except: Código que se ejecuta si hay un error.
- else: Se ejecuta si NO hubo error.
- finally: Se ejecuta SIEMPRE.
"""

print("\n--- Intento de división ---")
try:
    a, b = input("Introduce dos números para dividir (ej: 10 2): ").split()
    res = int(a) / int(b)
except Exception as e:
    print(f"Error detectado: {e}") # Captura el error (ej: división por cero)
else:
    print(f"Resultado: {res}")


"""
4. DEFINICIÓN: OBJETOS ITERADORES
Un objeto que permite recorrer una colección elemento por elemento.
Cuando se agotan los elementos, lanza la excepción 'StopIteration'.
"""

# Ejemplo de Iterador manual
nums = [10, 20, 30]
it = iter(nums) # Convertimos la lista en iterador

print("\n--- Recorrido de Iterador ---")
try:
    print(next(it)) # 10
    print(next(it)) # 20
    print(next(it)) # 30
    print(next(it)) # Aquí lanza el error StopIteration
except StopIteration:
    print("Iteración terminada: No hay más elementos.")