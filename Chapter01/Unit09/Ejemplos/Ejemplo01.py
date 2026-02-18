"""
El módulo random se usa para generar números al azar o mezclar elementos.
Para usarlo de forma cómoda, solemos abreviarlo como rd usando el comando
import random as rd.Funciones principales:

    random():Genera un número decimal entre 0 y 1.randrange(): Devuelve un número entero dentro de un rango específico.
    randint(a, b): Devuelve un número entero aleatorio $N$ tal que $a \leq N \leq b$.
    shuffle(seq): Mezcla al azar los elementos de una lista.
    choice(seq): Elige un elemento al azar de una lista o secuencia.
    sample(): Selecciona una cantidad específica de elementos al azar.
"""

import random as rd

# ==========================================
# EJEMPLOS DE LAS FUNCIONES DEL MÓDULO RANDOM
# ==========================================

# 1. random() - Ya lo tienes, pero aquí está para completar la lista
# Genera un decimal entre 0.0 y 1.0 (sin incluir el 1.0)
probabilidad = rd.random()
print(f"1. random(): {probabilidad}")

# 2. randrange(inicio, fin, paso) - También lo tienes
# Útil para rangos con saltos (como solo pares o solo múltiplos de 5)
numero_par = rd.randrange(0, 11, 2)
print(f"2. randrange(): {numero_par}")

# 3. randint(a, b)
# Devuelve un entero incluyendo AMBOS extremos (a y b)
# Ideal para simular dados o sorteos directos
dado = rd.randint(1, 6)
print(f"3. randint(1, 6): Sacaste un {dado}")

# 4. shuffle(seq)
# Mezcla una lista "in-place" (cambia la lista original)
# Muy útil para barajar cartas o turnos de juego
frutas = ["Manzana", "Plátano", "Cereza", "Mango"]
rd.shuffle(frutas)
print(f"4. shuffle(): Lista mezclada -> {frutas}")

# 5. choice(seq)
# Elige UN solo elemento al azar de una lista existente
# Perfecto para seleccionar un ganador o una respuesta aleatoria
bts = ['V', 'J-Hope', 'RM', 'Jungkook', 'Jin', 'Jimin', 'Suga']
ganador = rd.choice(bts)
print(f"5. choice(): El integrante elegido es {ganador}")

# 6. sample(seq, k)
# Selecciona 'k' elementos de una lista sin repetir ninguno
# Útil para sorteos de varios premios o elegir un equipo
equipo_pequeño = rd.sample(bts, 3)
print(f"6. sample(): Los 3 seleccionados son {equipo_pequeño}")