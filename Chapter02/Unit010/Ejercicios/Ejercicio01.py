s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

shortest = s_list[0]

# Recorro la lista
for s in s_list:
    if len(s) < len(shortest):
        shortest = s

# 4. Imprimimos el resultado con el formato solicitado
print(f"The shortest string : {shortest}")