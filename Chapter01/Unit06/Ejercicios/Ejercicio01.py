"""
Si la puntuación de un usuario (game_score) es mayor a $1000$ puntos, imprime: 'You are a master.' (Eres un maestro).
"""

game_score = int(input("Enter game score : "))
print(f"game_score = {game_score}")

if game_score > 1000:
    print("You are a master.")