"""
Dada la lista n_list que se muestra abajo,
escribe un código que genere una nueva lista result_list que contenga solo los elementos de n_list que no estén duplicados.
"""

n_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
result_list = []

for number in n_list:
    if number not in result_list:
        result_list.append(number)

print(f"n_list = {n_list}")
print(f"result_list = {result_list}")
