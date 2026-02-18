name = input("Introduce un nombre: ")
height_cm = int(input("Introduce tu altura (en cm): "))
height_m = height_cm / 100
weight = int(input("Introduce tu peso(kg): "))
bmi = weight / (height_m ** 2)
print(name, f"'s BMI is {bmi}")