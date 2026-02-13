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