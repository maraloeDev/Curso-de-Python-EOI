"""
Escribe un código que reciba el valor n a través de la entrada del teclado del usuario.
Retorna True si el entero n dado es impar y retorna False si el entero es par. Para los casos donde n es 20 y 21
"""

n = int(input("Introduce un número: "))

es_impar = n % 2 == 0
print(f"El numero {n} es {es_impar}")