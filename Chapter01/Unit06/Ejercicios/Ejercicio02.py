"""
Escribe un programa que reciba cualquier número entero $x$ entre $-100$ y $100$ y:Imprima $x$ en pantalla.Imprima "
...is a natural number" (...es un número natural)
si $x$ es un entero mayor que cero.De lo contrario, deja que simplemente imprima $x$ como en $x = -10$.
"""

x = int(input("Enter integer: "))
print(f"x = {x}")

if x > 0:
    print(f"{x} is a natural number.")