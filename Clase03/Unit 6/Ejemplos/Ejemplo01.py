# 1. Pedimos el número entero

x = int(input("Enter integer: "))
if -100<= x <= 100:
    # 2. Imprimimos el valor de x siempre (Paso obligatorio)
    print(f"x = {x}")
    # 3. Condicional: Solo si es mayor que 0 (número natural)

    if x > 0:

        print(f"{x} is a natural number.")
else:

    print("The number is out of the specified range.")


game_score = int(input("Enter game score : "))

print(f"game_score = {game_score}")


if game_score > 1000:

    print("You are a master.")
lista = input("Introduce una lista de números separados por espacios: ").split()
print(lista)
lista = input("Introduce una lista de números separados por espacios: ").split(',')

print(lista)