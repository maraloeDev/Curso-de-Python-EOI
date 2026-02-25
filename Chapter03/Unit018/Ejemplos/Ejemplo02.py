### CÁLCULO DE FIBONACCI (Primeros 5 números) ###

def fibonacci_cinco():
    n = 5
    a, b = 0, 1
    print(f"Secuencia de Fibonacci (primeros {n} números):")

    for i in range(n):
        print(a, end=" ")
        # Actualizamos los valores: el nuevo 'a' es 'b', y el nuevo 'b' es la suma
        a, b = b, a + b
    print() # Salto de línea

# Ejecución
fibonacci_cinco()