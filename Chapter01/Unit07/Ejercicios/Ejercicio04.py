"""
Escribe un programa que reciba un punto con coordenadas x e y,
Determina a qué cuadrante (1, 2, 3 o 4) pertenece el punto. etermine a qué cuadrante (1, 2, 3 o 4) pertenece el punto.
"""

entrada = input("Enter x,y coordinates: ").split()
x = int(entrada[0])
y = int(entrada[1])

# Usamos match con una tupla (x, y)
match (x, y):
    case (x, y) if x > 0 and y > 0:
        print("In the first quadrant")
    case (x, y) if x < 0 < y:
        print("In the second quadrant")
    case (x, y) if x < 0 and y < 0:
        print("In the third quadrant")
    case (x, y) if x > 0 > y:
        print("In the fourth quadrant")
    case (0, _):
        print("On the Y axis")
    case (_, 0):
        print("On the X axis")