"""
Recibe un número entero. Si el entero es un múltiplo de $5$, devuelve True (Verdadero). Si no, devuelve False (Falso).
"""

n = int(input("Introduce un numero: "))

multiplo5 = (n % 5 == 0)
print(f"El numero {n} es multiplo de 5? = {multiplo5}")