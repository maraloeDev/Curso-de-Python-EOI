n = int(input("Introduce un numero: "))

#Inicializamos un contador
contador = 0

# Mientras el contador sea menor o igual que 10, entonces, me imprimes n * contador
while contador <= 10 :
    print(f"{n} * {contador} = {n * contador}")
    contador+=1 # Incremento el contador a 1