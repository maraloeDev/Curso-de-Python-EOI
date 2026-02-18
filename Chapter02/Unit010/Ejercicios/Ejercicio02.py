s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

maxlength = s_list[0]

# Recorro la lista
for s in s_list:
    if len(s) > len(maxlength):
        maxlength = s

print(f"The shortest string : {maxlength}")