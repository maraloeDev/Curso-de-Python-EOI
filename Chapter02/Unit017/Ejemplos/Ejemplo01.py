import string

# Definimos la función que busca la letra en la cadena original
# y devuelve su equivalente en la cadena desplazada
def cipher(a):
    idx = src_str.index(a)
    return dst_str[idx]

# Configuramos las cadenas de referencia
src_str = string.ascii_uppercase
# Se crea el abecedario desplazado: toma desde la 'D' hasta el final y le pega 'ABC' al final
dst_str = src_str[3:] + src_str[:3]

# Solicitamos la entrada al usuario
src = input('Enter a sentence: ')
print('Encrypted text: ', end='')

# Recorremos cada carácter de la frase
for ch in src:
    if ch in src_str:
        # Si es una letra mayúscula, la ciframos
        print(cipher(ch), end='')
    else:
        # Si es un espacio, número o signo (como '!'), lo dejamos igual
        print(ch, end='')

print()