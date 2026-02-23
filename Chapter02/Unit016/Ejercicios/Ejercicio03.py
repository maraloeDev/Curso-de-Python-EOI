"""
Hay una lista mylist con tuplas (m, n) como elementos, como se muestra a continuación.

Si hay una tupla con el valor (a, b) y los valores a, b son ingresados por el usuario, imprime:
"There is an element (a, b) at the xth." (Hay un elemento (a, b) en la posición x).

Si no hay un (a, b) pero sí existe un (b, a), imprime: "There is no (a, b) but (b, a) there is at yth."
(No hay (a, b) pero hay (b, a) en la posición y).

Si no hay ni (a, b) ni (b, a), imprime: "There is no (a, b) nor (b, a)" (No hay ni (a, b) ni (b, a)).

mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]
"""

mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]

posiciones = {0: "first", 1: "second", 2: "third", 3: "fourth", 4: "fifth"}

entrada = input("Enter two integers: ").split()
a, b = int(entrada[0]), int(entrada[1])

tuple_ab = (a, b)
tuple_ba = (b, a)

# Lógica de búsqueda
if tuple_ab in mylist:
    idx = mylist.index(tuple_ab)
    print(f"There is {tuple_ab} at the {posiciones[idx]}.")

elif tuple_ba in mylist:
    idx = mylist.index(tuple_ba)
    print(f"There is no {tuple_ab} but there is {tuple_ba} at the {posiciones[idx]}.")

else:
    print(f"There is no {tuple_ab} nor {tuple_ba}")