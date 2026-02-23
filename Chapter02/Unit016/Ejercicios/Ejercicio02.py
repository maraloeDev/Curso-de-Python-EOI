"""
Escribe los resultados computacionales de los siguientes dos conjuntos. Encuentra los resultados del 1) al 7).
s1 = {10, 20, 30, 40}

s2 = {30, 40, 50, 60, 70}
"""

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))