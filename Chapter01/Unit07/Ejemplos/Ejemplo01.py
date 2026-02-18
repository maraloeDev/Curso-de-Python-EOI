"""
Este programa asigna una letra de calificación según la puntuación (score) ingresada:

A: 90 o más.

B: Menos de 90 y 80 o más.

C: Menos de 80 y 70 o más.

D: Menos de 70 y 60 o más.

F: Menos de 60.

Observaciones del texto:

La calificación 'B' para 88 puntos se imprime correctamente.

Sin embargo, este código se ha vuelto más complejo y difícil de leer.

Si hay una expresión condicional incorrecta, el error es difícil de identificar.

La posibilidad de errores aumenta porque necesitas identificar el significado de cada sentencia if por separado.

Solución: Para resolver este problema, aplica la sentencia if-elif-else.
"""

score = int(input('Enter score : '))

if score >= 90:
    grade = 'A'
if 90 > score >= 80:
    grade = 'B'
if 80 > score >= 70:
    grade = 'C'
if 70 > score >= 60:
    grade = 'D'
if score < 60:
    grade = 'F'

print('Your grade is: ', grade)