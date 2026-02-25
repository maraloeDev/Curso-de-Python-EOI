"""
RESUMEN DE CONCEPTOS: FACTORIALES, FUNCIONES Y MÉTODOS
"""

# --- 1.2. El Factorial con bucle 'for' ---
# El factorial de n (n!) es el producto de todos los enteros desde 1 hasta n.

def calcular_factorial_demo():
    # Pedir entrada al usuario
    n = int(input('Introduce un número para calcular su factorial: '))
    fact = 1

    # Bucle for: de 1 a n, la variable 'fact' se multiplica acumulando i
    for i in range(1, n + 1):
        fact = fact * i

    # Mostrar resultado usando el método .format()
    print('{}! = {}'.format(n, fact))


# --- 5.1. Diferencia entre Función y Método ---
# Ambos realizan acciones para tareas específicas, pero su estructura difiere.

# 1. FUNCIÓN: Un módulo independiente que recibe parámetros y devuelve resultados.
def mi_funcion_independiente(x, y):
    return x + y

# 2. MÉTODO: Una función "adjunta" a un objeto en programación orientada a objetos.
class EjemploObjeto:
    def __init__(self, valor):
        self.valor = valor # Esta es una 'instancia' con un valor específico

    def mi_metodo(self):
        # Un método puede llamar a objetos con diferentes valores (instancias)
        return f"El valor de este objeto es: {self.valor}"

# --- EJECUCIÓN ---
if __name__ == "__main__":
    # Ejemplo de Función
    resultado_func = mi_funcion_independiente(5, 10)
    print(f"Resultado de función: {resultado_func}")

    # Ejemplo de Método
    objeto_a = EjemploObjeto(100)
    print(objeto_a.mi_metodo()) # Se llama a través del objeto

    # Ejemplo de Factorial
    calcular_factorial_demo()