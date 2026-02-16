""""
Introduce una palabra y te dire si el vocal o consonante"""

letra = (input('Escribe una letra:')).lower()

def es_vocal(letra):

    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':

        print(f'La letra {letra} es una vocal')

    else:

        print(f'La letra {letra} es una consonante')



es_vocal(letra)