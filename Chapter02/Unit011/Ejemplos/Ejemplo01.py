# 1. RANGOS E ÍNDICES
# range(1, 10) genera números del 1 al 9
numeros = list(range(1, 10))

# Indexación positiva: 0, 1, 2...
# Indexación negativa: -1 (último), -2 (penúltimo)
print(f"Primero: {numeros[0]}, Último: {numeros[-1]}")

# 2. DIFERENCIA CLAVE: APPEND vs EXTEND
lista_1 = [1, 2]
lista_1.append([3, 4]) # Resultado: [1, 2, [3, 4]] -> Lista anidada

lista_2 = [1, 2]
lista_2.extend([3, 4]) # Resultado: [1, 2, 3, 4] -> Lista plana

# 3. LÓGICA DE ELEMENTOS VACÍOS (Ejercicio Q2)
# Python considera False a: [], (), "", 0
# Cualquier contenido es True: (1,), "a", [0]
items = [(), (1,), [], "hola"]
limpios = []
for i in items:
    if i: # Si 'i' tiene contenido (es True)
        limpios.append(i)

# 4. DUPLICADOS (Ejercicio Q3)
# Usar 'not in' es la mejor forma de filtrar
original = [1, 1, 2, 3, 3]
unicos = []
for n in original:
    if n not in unicos:
        unicos.append(n)

print(f"Sin duplicados: {unicos}")