s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

shortest_strings = []

# Busco todas las que tengan longitud 3
for s in s_list:
    if len(s) == 3:
        shortest_strings.append(f"'{s}'")

#Las unimos con una coma
resultado = ", ".join(shortest_strings)

print(f"The shortest strings : {resultado}")