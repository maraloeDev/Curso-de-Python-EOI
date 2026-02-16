"""
El Teorema de Pitágoras establece que el cuadrado de la hipotenusa c
de cualquier triángulo rectángulo es igual a la suma del cuadrado de la base $a$ más el cuadrado de la altura $b$.
 Escribe un código que calcule la longitud de la hipotenusa recibiendo la base y la altura como números enteros.
"""

base = int(input("Introduce la base: "))
altura = int(input("Introduce la altura: "))
resultado = pow(base, 2) + pow(altura,2)

print(f"La longitud de la hipotenusa es de {resultado}")

#print(f"La longitud de la hipotenusa es de {pow(base, 2) + pow(altura,2)}")
