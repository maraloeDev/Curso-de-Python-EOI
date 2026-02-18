"""
Escribe un programa que realice suma, resta, multiplicación y división.

El programa debe imprimir el resultado de la operación entre dos enteros positivos

basándose en un "número de operación" (1, 2, 3 o 4) ingresado por el usuario.

Si se ingresa un número distinto a 1, 2, 3 o 4, debe imprimir: 'Entered an incorrect number' (Has ingresado un número incorrecto).

Instrucción de entrada: Para ingresar los dos números, escribe uno, presiona "Enter" y escribe el otro.
"""

print("1) Addition    2) Subtraction    3) Multiplication    4) Division")

operacion = int(input("Enter the desired number of operation : "))

match operacion:
    case 1 | 2 | 3 | 4:

        print("Enter two numbers for operation.")
        num1 = int(input())
        num2 = int(input())

        match operacion:
            case 1:
                print(f"{num1} + {num2} = {num1 + num2}")
            case 2:
                print(f"{num1} - {num2} = {num1 - num2}")
            case 3:
                print(f"{num1} * {num2} = {num1 * num2}")
            case 4:
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by zero.")
    case _:
        print("Entered an incorrect number.")